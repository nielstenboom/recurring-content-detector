import os
import itertools
import operator
import numpy as np
import pickle
import faiss

# internal imports
import config
import featurevectors
import video_functions
import detection



# the video files used for the detection
videos = [f for f in os.listdir(config.VIDEO_DIR) if os.path.isfile(os.path.join(config.VIDEO_DIR, f))]
# location of the vector directory
vectors_dir = os.path.join(config.VIDEO_DIR, "resized", "feature_vectors_framejump{}".format(config.FRAMEJUMP))

for file in videos:
    # set the video path files
    file_full = os.path.join(config.VIDEO_DIR, file)
    file_resized = os.path.join(config.VIDEO_DIR, "resized", file)

    # make sure folder of experimentname exists or create otherwise
    os.makedirs(os.path.dirname(file_resized), exist_ok=True)
    
    # if there is no resized video yet, then resize it
    if not os.path.isfile(file_resized):
        video_functions.resize(file_full, file_resized)

    # from the resized video, construct feature vectors
    featurevectors.construct_feature_vectors(   
        file_resized, "feature_vectors_framejump{}".format(config.FRAMEJUMP), featurevectors.color_hist)


vector_files = [os.path.join(vectors_dir,e+'.p') for e in videos]
vectors = []

# the lengths of each vector, will be used to query each episode
lengths = []

# concatenate all the vectors into a single list multidimensional array
for f in vector_files:
    h = np.array(pickle.load(open(f, "rb")), np.float32)
    lengths.append(h.shape[0])
    vectors.append(h)

vectors = np.vstack(vectors)

results = []
for i, length in enumerate(lengths):
    i += 1
    s = sum(lengths[:i-1])
    e = sum(lengths[:i])

    # query consists of one episode
    query = vectors[s:e]
    # rest of the feature vectors
    rest = np.append(vectors[:s], vectors[e:], axis=0)

    # build the faiss index, set vector size
    vector_size = query.shape[1]
    index = faiss.IndexFlatL2(vector_size)    
    # add vectors of the rest of the episodes to the index
    index.add(rest)

    # we want to see k nearest neighbors
    k = 1
    # search with for matches with query
    scores, indexes = index.search(query, k)
    
    result = scores[:,0]    
    results.append((videos[i-1], result))


for video, result in results:
    framejump = config.FRAMEJUMP
    framerate = video_functions.get_framerate(os.path.join(config.VIDEO_DIR, video))
    threshold = np.percentile(result, config.PERCENTILE)

    # all the detections
    below_threshold = result < threshold
    # Merge all detections that are less than 10 seconds apart
    below_threshold = detection.fill_gaps(below_threshold, int((framerate/config.FRAMEJUMP) * 10))

    nonzeros = [[i for i, value in it] for key, it in itertools.groupby(
        enumerate(below_threshold), key=operator.itemgetter(1)) if key != 0]

    detected_beginning = []
    detected_end = []

    for nonzero in nonzeros:
        start = nonzero[0]
        end = nonzero[-1]

        #result is in first 20% of the video
        occurs_at_beginning = end < len(result) / 5
        #the end of this timestamp ends in the last 15 seconds             
        ends_at_the_end = end > len(result) - 15 * (framerate/framejump) 

        if (end - start > (15 * (framerate / framejump)) #only count detection when larger than 15 seconds             
            and (occurs_at_beginning or ends_at_the_end)): #only use results that are in first 1/5 part or end at last 15 s            

            start = start / (framerate / framejump)
            end = end / (framerate / framejump)

            if occurs_at_beginning:
                detected_beginning.append((start,end))
            elif ends_at_the_end:
                detected_end.append((start,end))


    detected = detection.get_two_longest_timestamps(detected_beginning) + detected_end

    print("Detections for: {}".format(video))
    for start,end in detected:
        
        print("{} \t \t - \t \t {}".format(detection.to_time_string(start), detection.to_time_string(end)))

    print()

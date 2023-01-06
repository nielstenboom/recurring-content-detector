# Recurring content detector (credits, recaps and previews detection)

This repository contains the code that was used to conduct experiments for a [master's thesis](https://github.com/nielstenboom/masterthesis/raw/master/main.pdf). The goal was to detect recaps, opening credits, closing credits and previews from video files in an unsupervised manner. This can be used to automate the labeling for the skip functionality of a VOD streaming service for example.

## Quickstart with Docker

To try this out with Docker on your own data, copy the video files of one season to a folder in the current directory named `videos`, then create a script `detect.py` with the contents:

```python
import recurring_content_detector as rcd

results = rcd.detect("videos")

print(results)
```
Now you can run the detector by running the docker command:
```
docker run -it -v "$(pwd)":/opt/recurring-content-detector nielstenboom/recurring-content-detector:latest python detect.py
```
It'll first downsize the videos using ffmpeg, then it will convert the videos to feature vectors and then the algorithm for detecting the recurring content is applied, the `results` variable contains the intervals of all the recurring parts.

## Local Installation

To install the package, do the following steps:

```bash
pip install mkl
pip install git+https://github.com/nielstenboom/recurring-content-detector.git@v1.1.1
```

It is also possible to build a docker container that does all the steps for you with the [Dockerfile](Dockerfile) in the directory.

Make sure [ffmpeg](https://ffmpeg.org/) is in the PATH variable.

Run `pip uninstall recurring-content-detector` to uninstall the package.

## Recurring content detection

With this code it is possible to detect recaps, opening credits, closing credits and previews in video files from a TV-show unsupervised up to a certain extent. The following image gives a schematic overview of how it works: 

<p align="center">
<img src="images/thesisdiagram.png?raw=true">
</p>

You can run the detector in a python program in the following way:

```python
import recurring_content_detector as rcd
rcd.detect("/directory/with/season/videofiles")
```
This will run the detection by building the color histogram feature vectors. Make sure the video files you used can be sorted in the right alphabetical order similar as to when they play in the season! So episode_1 -> episode_2 -> episode_3 -> etc.. You'll get weird results otherwise.


The feature vector function can also be changed:
```python
# options for the function are ["CH", "CTM"]
rcd.detect("/directory/with/season/videofiles", feature_vector_function="CTM")
```

The `detect` function has many more parameters that can be tweaked, the defaults it has, are the parameters I got the best results with on my experiments.

```python
def detect(video_dir, feature_vector_function="CH", annotations=None, artifacts_dir=None, 
            framejump=3, percentile=10, resize_width=320, video_start_threshold_percentile=20, 
            video_end_threshold_seconds=15, min_detection_size_seconds=15):
"""
The main function to call to detect recurring content. Resizes videos, converts to feature vectors
and returns the locations of recurring content within the videos.

arguments
---------
video_dir : str
    Variable that should have the folder location of one season of video files.

annotations : str
    Location of the annotations.csv file, if annotations is given then it will evaluate 
    the detections with the annotations.
    
feature_vector_function : str
    Which type of feature vectors to use, options: ["CH", "CTM", "CNN"], default is color histograms (CH) 
    because of balance between speed and accuracy. This default is defined in init.py.

artifacts_dir : str
    Directory location where the artifacts should be saved. Default location is the location defined 
    with the video_dir parameter.

framejump : int
    The frame interval to use when sampling frames for the detection, a higher number means that 
    less frames will be taken into consideration and will improve the processing time. 
    But will probably cost accuracy.

percentile : int
    Which percentile of the best matches will be taken into consideration as recurring content. 
    A high percentile will means a higher recall, lower precision. 
    A low percentile means a lower recall and higher precision.

resize_width: int
    Width to which the videos will be resized. A lower number means higher processing speed but 
    less accuracy and vice versa.

video_start_threshold_percentile: int
    Percentage of the start of the video in which the detections will be marked as detections. 
    As recaps and opening credits only occur at the first parts of video files, this parameter can alter 
    that threshold. So putting 20 in here means that if we find recurring content in the first 20% of 
    frames of the video, it will be marked as a detection. If it's detected later than 20%, then the 
    detection will be ignored.

video_end_threshold_seconds: int
    Number of seconds threshold in which the final detection at the end of the video should end for it 
    to count. Putting 15 here means that a detection at the end of a video will only be marked as a 
    detection if the detection ends in the last 15 seconds of the video.

min_detection_size_seconds: int
    Minimal amount of seconds a detection should be before counting it as a detection. As credits & 
    recaps & previews generally never consist of a few seconds, it's wise to pick at least a number 
    higher than 10.

returns
-------
dictionary
    dictionary with timestamp detections in seconds list for every video file name
    
    {"episode1.mp4" : [(start1, end1), (start2, end2)], 
     "episode2.mp4" :  [(start1, end1), (start2, end2)],
     ...
     "episode10.mp4" : [(start1, end1), (start2, end2)]
    }
    """
```

## Annotations

If you want to quantitively test out how well this works on your own data, fill in the [annotations](annotations_example.csv) file and supply it as the second parameter.
```python
rcd.detect("directory/with/season/videofiles", annotations = "path/to/annotations.csv")
```

When the program is done, it will give an example with the same outline as the example below:

 ```
Detections for: episode1.mp4
0:01:21.600000           -               0:02:20.880000
0:02:49.320000           -               0:03:15.480000

Detections for: episode2.mp4
0:00:00                  -               0:01:16.920000
0:01:38.040000           -               0:02:37.440000

Detections for: episode3.mp4
0:00:00                  -               0:01:27.840000
0:01:51.120000           -               0:02:50.760000
0:42:26.400000           -               0:42:54

Total precision = 0.862
Total recall = 0.853
 ```

## Tests

There's a few tests in the test directory. They can also be run in the docker container:
```
docker run -it -v $(pwd):/opt/recurring-content-detector nielstenboom/recurring-content-detector:latest python -m pytest
```
 
## Credits
- https://github.com/facebookresearch/faiss for the efficient matching of the feature vectors 

## Final words
If you use and like my project or want to discuss something related, I would  ❤️  to hear about it! You can send me an email at nielstenboom@gmail.com.

import os
import config
import featurevectors
import video_functions
import cv2

files = [f for f in os.listdir(config.VIDEO_DIR) if os.path.isfile(os.path.join(config.VIDEO_DIR, f))]

for file in files:
    file_full = os.path.join(config.VIDEO_DIR, file)
    file_resized = os.path.join(config.VIDEO_DIR, "resized", file)

    # make sure folder of experimentname exists or create otherwise
    os.makedirs(os.path.dirname(file_resized), exist_ok=True)
    
    if not os.path.isfile(file_resized):
        video_functions.resize(file_full, file_resized)

    featurevectors.construct_feature_vectors(   
        file_resized, "feature_vectors_framejump{}".format(config.FRAMEJUMP), featurevectors.color_hist)

# the uniform sampling rate, every FRAMEJUMP frames a frame will be taken into account
FRAMEJUMP = 3

# width of video to resize to, any width other than 224 will keep the aspect ratio intact
# use 224 in combination with the CNN feature vectors, 320 was used with the others
RESIZE_WIDTH = 320

# percentile of the lowest values in the vector results to mark as detections
PERCENTILE = 10

# Which type of feature vectors to use options: ["CH", "CTM", "CNN"]
FEATURE_VECTOR_FUNCTION = "CH"



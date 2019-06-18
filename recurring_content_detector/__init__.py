from . import detector
from . import config

def detect(video_dir, annotations = None, feature_vector_function = "CNN"):
    
    old_width = config.RESIZE_WIDTH
    
    # make sure resize width of 224 is used with CNN
    if feature_vector_function == "CNN":
        config.RESIZE_WIDTH = 224

    result = detector.detect(video_dir, feature_vector_function, annotations)

    # set config variable back to the old value,
    # so when reusing the module, there is no unexpected behavior.
    config.RESIZE_WIDTH = old_width

    return result


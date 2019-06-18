from . import detector

def detect(video_dir, annotations = None, feature_vector_function = "CNN"):
    return detector.detect(video_dir, feature_vector_function, annotations)


from . import detector

def detect(video_dir, annotations = None, feature_vector_function = None):
    return detector.detect(video_dir, annotations, feature_vector_function)


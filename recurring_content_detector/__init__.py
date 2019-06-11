from . import detector

def detect(video_dir, annotations = None):
    return detector.detect(video_dir, annotations)


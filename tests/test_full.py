import recurring_content_detector as rcd

def test_full_run():
    results = rcd.detect("tests/data", video_start_threshold_percentile=50, min_detection_size_seconds=3)

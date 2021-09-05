import recurring_content_detector as rcd

def test_full_run():
    """
    Do full run on 2 small videos 
    and check if detections are in line with expectations

    Expectations:
        Detections for: video0.mp4
        0:00:00                  -               0:00:05.405400
        0:00:46.046000           -               0:00:50.850800

        Detections for: video1.mp4
        0:00:00                  -               0:00:05.605600
        0:00:29.629600           -               0:00:34.334300
    """
    results = rcd.detect("tests/data", video_start_threshold_percentile=50, min_detection_size_seconds=3)
    vid0 = results["video0.mp4"]
    vid1 = results["video1.mp4"]

    assert 5.2 < abs(vid0[0][0] - vid0[0][1]) < 5.8
    assert 4.5 < abs(vid0[1][0] - vid0[1][1]) < 5.5

    assert 5.2 < abs(vid1[0][0] - vid1[0][1]) < 5.8
    assert 4.5 < abs(vid1[1][0] - vid1[1][1]) < 5.5
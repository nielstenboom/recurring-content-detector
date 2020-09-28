from recurring_content_detector.detector import fill_gaps, get_two_longest_timestamps
import numpy as np

def test_fill_gaps_regular():
    input = np.array([0,0,1,0,0,0,0,1,0,0])
    expected = [0,0,1,1,1,1,1,1,0,0]

    output = fill_gaps(input, lookahead=6)

    assert expected == output.tolist()


def test_fill_gaps_largerlookahaead():
    input = np.array([0,0,1,0,0,0,0,1,0,0])
    expected = [0,0,1,1,1,1,1,1,0,0]

    output = fill_gaps(input, lookahead=20)

    assert expected == output.tolist()



def test_fill_gaps_smalllookahaead():
    input = np.array([0,0,1,0,0,0,0,1,0,0])
    expected = [0,0,1,0,0,0,0,1,0,0]

    output = fill_gaps(input, lookahead=3)

    assert expected == output.tolist()

def test_fill_gaps_multiple():
    input = np.array([0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1])
    expected = [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]

    output = fill_gaps(input, lookahead=6)

    assert expected == output.tolist()


def test_get_two_longest_timestamps_regular():
    input = [(0,10), (0,5), (20,21)]
    expected = [(0,10), (0,5)]

    output = get_two_longest_timestamps(input)

    assert expected == output

def test_get_two_longest_timestamps_singlevalue():
    input = [(0,10)]
    expected = [(0,10)]

    output = get_two_longest_timestamps(input)

    assert expected == output
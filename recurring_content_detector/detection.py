
import datetime

def max_two_values(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    result1 = k[v.index(max(v))]
    del d[result1]

    v=list(d.values())
    k=list(d.keys())
    result2 = k[v.index(max(v))]
    return [result1, result2]


def fill_gaps(sequence, lookahead):
    i = 0
    while i < len(sequence) - lookahead:
        current = sequence[i]
        next = sequence[i + 1 : i + lookahead].tolist()
        
        if current and True in next:
            x = 0
            while not next[x]:
                sequence[i + 1 + x] = True
                x = x + 1
                
        i = i + 1

    return sequence

def get_two_longest_timestamps(timestamps):
    # if size is smaller or equal to 2, return immediately
    if len(timestamps) <= 2:
        return timestamps

    d = {}
    for start,end in timestamps:
        d[(start,end)] = end - start

    return max_two_values(d)

def to_time_string(seconds):
    """
    Given seconds in number, returns a string in the format hh:mm:ss (example: 01:30:45)
    """
    return str(datetime.timedelta(seconds=seconds))
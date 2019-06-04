


def merge_consecutive_timestamps(timestamps):
    """
    Merges consecutive timestamps in a list if they're less than 2 seconds apart
    Example: [(0,5), (5,10), (20,30)] gets combined into [(0,10),[20,30]
    """
    result = []
    i = 0
    while i < len(timestamps):
        (start, end) = timestamps[i]

        # check if we're not already at the last element
        if i < len(timestamps) - 1:
            (start_next, end_next) = timestamps[i + 1]
            # merge if less than 2 seconds apart
            if abs(end - start_next) < 2:
                result.append((start, end_next))
                i += 1
            else:
                result.append((start,end))
            
        else:
            result.append((start, end))

        i += 1

    return result


def to_seconds(time):
    """
    Converts string of format hh:mm:ss to total number of seconds
    """
    if time == 'None':
        return -1
    try:
        hours = int(time.split(":")[0])
        minutes = int(time.split(":")[1])
        seconds = int(float(time.split(":")[2]))
        return hours*60*60 + minutes * 60 + seconds
    except:
        if math.isnan(time):
            return -1

def get_skippable_timestamps_by_filename(filename, df):
    row = df.loc[df['filename'] == filename].to_dict(orient='records')[0]
    result = []
    
    if not row["recap_start"] == -1:
        result.append((row["recap_start"], row["recap_end"]))
    if not row["openingcredits_start"] == -1:
        result.append((row["openingcredits_start"], row["openingcredits_end"]))
    if not row["preview_start"] == -1:
        result.append((row["preview_start"], row["preview_end"]))
    if not row["closingcredits_start"] == -1:
        result.append((row["closingcredits_start"], row["closingcredits_end"]))
        
    return merge_consecutive_timestamps(result)

def get_annotations():
    annotations = pd.read_csv("annotations_legal_new_final.csv").dropna(how='all')
    annotations['recap_start'] = annotations['recap_start'].apply(to_seconds)
    annotations['recap_end'] = annotations['recap_end'].apply(to_seconds)
    annotations['openingcredits_end'] = annotations['openingcredits_end'].apply(to_seconds)
    annotations['openingcredits_start'] = annotations['openingcredits_start'].apply(to_seconds)
    annotations['preview_start'] = annotations['preview_start'].apply(to_seconds)
    annotations['preview_end'] = annotations['preview_end'].apply(to_seconds)
    annotations['closingcredits_end'] = annotations['closingcredits_end'].apply(to_seconds)
    annotations['closingcredits_start'] = annotations['closingcredits_start'].apply(to_seconds)
    return annotations
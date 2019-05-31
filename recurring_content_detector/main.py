import os

series_dir = "./videos_resized_w320/"
files = [f for f in os.listdir(series_dir) if os.path.isfile(os.path.join(series_dir, f))]
for file in files:
    construct_feature_vectors(file, series_dir, "color_histogram_binsize300_framejump{}".format(framejump), color_hist)
import cv2
import os
import subprocess
import ffmpeg
import os.path

video_input_dir = './videos_resized_w320/'
video_output_dir = './videos_resized_w224/'

# loops through the videos and resizes them with ffmpeg
for f in os.listdir(video_input_dir):
    if '.mp4' in f:
        video2 = cv2.VideoCapture(video_input_dir+f)
        framecount = int(video2.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video2.get(cv2.CAP_PROP_FPS)
        
        if framecount > 0 and not os.path.isfile(video_output_dir + f):
            print(f)
            try:
                stream = ffmpeg.input("./videos/{}".format(f))
                stream = ffmpeg.filter(stream, 'scale', w=224, h=224)
#                 stream = ffmpeg.filter(stream, 'scale', w=224, h="trunc(ow/a/2)*2")
                stream = ffmpeg.output(stream, video_output_dir + f)
                ffmpeg.run(stream)
            except Exception as e:
                print(e.stdout)
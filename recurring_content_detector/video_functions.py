import cv2
import os
import subprocess
import ffmpeg
import os.path

from . import config

def get_framerate(video_fn):
    """
    Return the video framerate given a video filename
    """
    video = cv2.VideoCapture(video_fn)
    return video.get(cv2.CAP_PROP_FPS)



def resize(input, output):
    """
    Resizes a video with ffmpeg
    """
    video2 = cv2.VideoCapture(input)
    framecount = int(video2.get(cv2.CAP_PROP_FRAME_COUNT))

    if framecount > 0:
        stream = ffmpeg.input(input)
        if config.RESIZE_WIDTH == 224:
            stream = ffmpeg.filter(stream, 'scale', w=224, h=224)
        else:
            stream = ffmpeg.filter(stream, 'scale', w=config.RESIZE_WIDTH, h="trunc(ow/a/2)*2")
        stream = ffmpeg.output(stream, output)
        ffmpeg.run(stream)
    else:
        raise Exception("Something is wrong with the video file: {}".format(input))
# Scripts to try and detect key frames that represent scene transitions
# in a video. Has only been tried out on video of slides, so is likely not
# robust for other types of video.

import cv2
import argparse
import json
import os
import numpy as np
import errno

#
# Does regular extraction of thumbnails
#
def getNumFrames(sourcePath):
    cap = cv2.VideoCapture(sourcePath)
    numFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(sourcePath, numFrames)
    cap.release()
    cv2.destroyAllWindows()
    return numFrames


parser = argparse.ArgumentParser()

parser.add_argument('-s','--source', help='source file', required=True)
parser.set_defaults(verbose=False)

args = parser.parse_args()

if args.verbose:
    info = getInfo(args.source)
    print("Source Info: ", info)

# Run the extraction
data = getNumFrames(args.source)


import argparse
import json
from os import listdir
from os.path import isfile, join


# Simple utility to read the thumbnails directory and extract the frame numbers
# from the filenames and write those numbers to a JSON file

parser = argparse.ArgumentParser()

parser.add_argument('-s','--source', help='source directory', required=True)
parser.add_argument('-d', '--dest', help='destination file', required=True)
args = parser.parse_args()

def filename_to_frame(filename):
    return int(filename[filename.rfind('-') + 1:len(filename) - 4])

def thumbs_to_frame(thumbs_dir):
    frames = [filename_to_frame(f) for f in listdir(join(thumbs_dir, 'images', 'full')) if isfile(join(thumbs_dir, 'images', 'full', f))]
    frames.sort()

    return frames


frames = [thumbs_to_frame(join(args.source, thumb_dir)) for thumb_dir in listdir(args.source) if not isfile(join(args.source, thumb_dir))]

handle = open(args.dest, 'w')
handle.write(json.dumps(frames))
handle.write('\n')
handle.close()


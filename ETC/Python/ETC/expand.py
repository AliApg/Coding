import argparse
import os
from datetime import datetime

import cv2

parser = argparse.ArgumentParser()

parser.add_argument("-in", "--input",
                    help="Input image directory", required=True)
parser.add_argument("-out", "--output", help="Output image directory")
parser.add_argument("-s", "--scale", help="Scale of the output image")

args = parser.parse_args()

if not os.path.isfile(args.input):
    raise (FileNotFoundError)

scale = int(args.scale) if args.scale and args.scale.isdigit() else 8

if args.output:
    out_dir = args.output

else:
    dir_ = str(args.input)[2:].rsplit('.', 1)
    out_dir = f'{dir_[0]}_out_{datetime.now().strftime(r"%m-%d-%Y_%H-%M-%S")}.{dir_[-1]}'


img = cv2.imread(args.input)

img_resized = cv2.resize(
    img, dsize=(img.shape[1]*scale, img.shape[0]*scale), interpolation=cv2.INTER_CUBIC)

cv2.imwrite(out_dir, img_resized)

print(f'\nImage saved: {out_dir}\nScale: {scale}\n')

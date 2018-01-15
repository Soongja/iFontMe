# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

import argparse
import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import collections
import random

reload(sys)
sys.setdefaultencoding("utf-8")


def draw_single_char(ch, font, canvas_size, x_offset, y_offset):
    img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((x_offset, y_offset), unichr(int(ch, 16)), (0, 0, 0), font=font)
    return img


def draw_example(ch, src_font, dst_font, canvas_size, x_offset, y_offset):
    dst_img = draw_single_char(ch, dst_font, canvas_size, x_offset, y_offset)
    src_img = draw_single_char(ch, src_font, canvas_size, x_offset, y_offset)
    example_img = Image.new("RGB", (canvas_size * 2, canvas_size), (255, 255, 255))
    example_img.paste(dst_img, (0, 0))
    example_img.paste(src_img, (canvas_size, 0))
    return example_img


def font2img(src, dst, charset,
             char_size, canvas_size, x_offset, y_offset,
             sample_count, sample_dir, label):
    src_font = ImageFont.truetype(src, size=char_size)
    dst_font = ImageFont.truetype(dst, size=char_size)

    count = 0

    for c in charset:
        if count == sample_count:
            break
        e = draw_example(c, src_font, dst_font, canvas_size, x_offset, y_offset)
        if e:
            e.save(os.path.join(sample_dir, "%d_%04d.jpg" % (label, count)))
            count += 1
            if count % 100 == 0:
                print("processed %d chars" % count)

parser = argparse.ArgumentParser(description='Convert font to images')
parser.add_argument('--src_font', dest='src_font', required=True, help='path of the source font')
parser.add_argument('--dst_font', dest='dst_font', required=True, help='path of the target font')
parser.add_argument('--shuffle', dest='shuffle', type=int, default=0, help='shuffle a charset before processings')
parser.add_argument('--char_size', dest='char_size', type=int, default=150, help='character size')
parser.add_argument('--canvas_size', dest='canvas_size', type=int, default=256, help='canvas size')
parser.add_argument('--x_offset', dest='x_offset', type=int, default=20, help='x offset')
parser.add_argument('--y_offset', dest='y_offset', type=int, default=20, help='y_offset')
parser.add_argument('--sample_dir', dest='sample_dir', help='directory to save examples')
parser.add_argument('--label', dest='label', type=int, default=0, help='label as the prefix of examples')
parser.add_argument('--unicode', dest='unicode', help='path of the unicode list')
parser.add_argument('--sample_count', dest='sample_count', type=int, default=12000, help='number of characters to draw')

args = parser.parse_args()

if __name__ == "__main__":
    charset = open(args.unicode).read().split('\n')
    if args.shuffle:
        random.shuffle(charset)
    font2img(args.src_font, args.dst_font, charset,
             args.char_size, args.canvas_size, args.x_offset, args.y_offset,
             args.sample_count, args.sample_dir, args.label)
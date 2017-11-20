from PIL import ImageFont, Image, ImageDraw
import os

width = 100
height = 120
black = (0,0,0)
white = (255,255,255)
font_name = "NanumGothic"
font_size = 100

data = open('./unicode_11172.txt')
unicode_list = data.read().split('\n')

if font_name not in os.listdir():
    os.mkdir(font_name)

for i in unicode_list:
    each_unicode = i

    font = ImageFont.truetype(font_name + ".ttf", font_size)
    img = Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), chr(int(each_unicode, 16)), font=font, fill=black)
    img.save(font_name + "/" + font_name + "_" + each_unicode + ".JPG")
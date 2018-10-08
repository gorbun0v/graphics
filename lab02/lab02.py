#!/usr/bin/python3

import sys
from PIL import Image, ImageDraw

def Average(arr, i, j, p):
    summ = 0
    error = 0
    for k in range(-1, 2):
        for q in range(-1, 2):
            try:
                summ += arr[i+k, j+k][p]
            except:
                error += 1
    res = summ // (9 - error)
    return res

filepath = sys.argv[1] 
image = Image.open(filepath)
width, height = image.size

pix = image.load()

result = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(result)

for i in range(width):
    for j in range(height):
        red = Average(pix, i, j, 0)
        green = Average(pix, i, j, 1)
        blue = Average(pix, i, j, 2)
        draw.point((i, j), (red, green, blue))

result.save('result.png', 'png')
result.close()
image.close()

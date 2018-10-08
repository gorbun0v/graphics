#!/usr/bin/python3

import sys
from PIL import Image, ImageDraw

def Average(pix, i, j):
	return int(sum(pix[i,j]) / len(pix[i,j]))


def GetCx(pix, i, j):
	cx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
	result = 0
	for k in range(3):
		for q in range(3):
			try:
				result += cx[k][q] * Average(pix, i+k-1, j+q-1)
			except:
				pass
	return result

def GetCy(pix, i, j):
	cx = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
	result = 0
	for k in range(3):
		for q in range(3):
			try:
				ave = Average(pix, i+k-1, j+q-1)
				result += cx[k][q] * ave
			except:
				pass
	return result

def Paint(photo, cursor):
	pix = photo.load()
	width, height = photo.size
	for i in range(width):
		for j in range(height):
			cx = GetCx(pix, i, j)
			cy = GetCy(pix, i, j)
			res = int((cx**2 + cy**2) ** 0.5)
			cursor.point((i, j),(res, res, res))





if __name__ == '__main__':
	filepath = sys.argv[1]
	photo = Image.open(filepath)
	
	width, height = photo.size
	result = Image.new('RGB', (width, height))
	draw = ImageDraw.Draw(result)
	Paint(photo, draw)

	result.save('result.png', 'png')
	result.close()
	photo.close()
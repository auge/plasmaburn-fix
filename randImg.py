#!/usr/bin/env python

import pypng.code.png as png
import numpy.random as nprnd

width = 1920
height = 1080
numFiles = 500

for n in range(numFiles):
	f = open("b{:03d}.png".format(n), 'wb')
	w = png.Writer(width, height)

	dat = []

	for i in range(height):
		dat.append(list(nprnd.randint(2, size=3*width) * 255))

	w.write(f, dat)
	f.close()

print("done")

#!/usr/bin/env python

import sys
import argparse
import pypng.code.png as png
import numpy.random as nprnd

#defaults:
defwidth = 1920
defheight = 1080
defnumFiles = 600

def arguments():
	"""
	parsing command line arguments
	"""
	parser = argparse.ArgumentParser(description="Generate random PNG images. Each pixel will be a random combination of either 0% or 100% red, green and blue.")
	parser.add_argument("-d", "--dim", type=int, nargs=2, dest="dim", default=[defwidth, defheight], help="Dimension (width, heigth) of images")
	parser.add_argument("-n", "--numFiles", type=int, dest="numFiles", default=defnumFiles, help="Number of images")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print debug info.")
	parser.add_argument("-s", "--stats", action="store_true", dest="stats", default=False, help="Compute statistics about color distribution (not yet implemented)")
	return parser.parse_args()


def main(args):
	"""
	create n random png-images wxh pixels
	"""
	numdigits = len(str(args.numFiles))
	strformat = "b{:0"+str(numdigits)+"d}.png"
	width = args.dim[0]
	height = args.dim[1]

	for n in range(args.numFiles):
		fname = strformat.format(n)
		if args.verbose:
			print(fname)
		f = open(fname, 'wb')
		w = png.Writer(width, height)

		dat = []

		for i in range(height):
			dat.append(list(nprnd.randint(2, size = 3 * width) * 255))

		w.write(f, dat)
		f.close()

	if args.verbose:
		print("done")


if __name__ == '__main__':
	args = arguments()
	main(args)


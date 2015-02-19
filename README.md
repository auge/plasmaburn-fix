# plasmaburn-fix

randImg.py can be invoked from command line in order to generated images to be used to fix a common problem with plasma tv screens [1].
The images can then be converted into a video-sequence using ffmpeg [2]:

```
ffmpeg -framerate 60 -i b%03d.png -s 1920x1080 -pix_fmt yuv420p test.mp4
```

You can play with the parameters if your TV or video-player supports different settings.


Command line interface implemented:

```
./randImg.py -h
usage: randImg.py [-h] [-d DIM DIM] [-n NUMFILES] [-v] [-s]

Generate random PNG images. Each pixel will be a random combination of either 0% or 100% red, green and blue.

optional arguments:
  -h, --help            show this help message and exit
  -d DIM DIM, --dim DIM DIM
                        Dimension (width, heigth) of images
  -n NUMFILES, --numFiles NUMFILES
                        Number of images
  -v, --verbose         Print debug info.
  -s, --stats           Compute statistics about color distribution (not yet implemented)
```

[1] http://en.wikipedia.org/wiki/Screen_burn-in

[2] https://www.ffmpeg.org/

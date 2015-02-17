# plasmaburn-fix

randImg.py can be invoked from command line in order to generated images to be used to fix a common problem with plasma tv screens [1].
The images can then be converted into a video-sequence using ffmpeg [2]:

ffmpeg -framerate 60 -i b%03d.png -s 1920x1080 -pix_fmt yuv420p test.mp4

You can play with the parameters if your TV or video-player supports different settings.


Currently, parameters are hard-coded. If the images (and the generated video-sequence) gives some positive results, I might add a command-line interface.


[1] http://en.wikipedia.org/wiki/Screen_burn-in
[2] https://www.ffmpeg.org/

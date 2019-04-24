import capture_image
from capture_image import capture_img

entry_camera = capture_img(r"Exit_picture1")
#uses start_capture funtion to take 5 pictures in an instance of 2 seconds 
#and store them in Exit_ picture1 folder 

entry_camera.start_capture(delay=0.4,count=5,sf=3.0,interval=0)

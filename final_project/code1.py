import capture_image
from capture_image import capture_img

entry_camera = capture_img(r"Entry_picture")
#uses start_capture funtion to take 5 pictures in an instance of 2 seconds 
#and store them in Entry_picture1
entry_camera.start_capture(delay=0.4,count=5,sf=1.3,interval=0)
import capture_image
from capture_image import capture_img

entry_camera = capture_img(r"Inside_picture1")
#uses start_capture funtion to take 2 pictures every 5 min with delay of  1 seccond  between each photo 
#and store them in inside_picture1 folder 1 
entry_camera.start_capture(delay=1,count=2,sf=1.3,interval=300)

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as im 
import cv2
import os 
from sklearn.externals import joblib
import capture_image
from capture_image import capture_img

# load the model from face_model folder
model = joblib.load("Face_model/facemodel.pkl")

folder = r"Exit_picture1"

file_names=os.listdir(folder)
#capture_img is a function that load the file, convert the image to  color gray , resize the image to 100by100 ,
#and reshap it to 1 to 10000
#appending the images to image file
Exit1 = capture_img(folder)
  

  

for imgname in file_names:
    img,img2 = Exit1.load_image(imgname)
    prediction = model.predict(img2)[0]
    cv2.imwrite("Exit_picture2//"+prediction+"_exit"+imgname[-7:],img)
    

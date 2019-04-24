import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as im 
import cv2
import os 
#uploads folder 
folder=r"Entry_picture"
file_names=os.listdir(folder)
print(len(file_names))
print(file_names)


file_names=os.listdir(folder)
#capture_img is a function that load the file, convert the image to  color gray , resize the image to 100by100 ,
#and reshap it to 1 to 10000
#appending the images to image file 
Entry = capture_img(folder)

trainimg = []
trainlb = []
for imgname in file_names:
    img = load_image(imgname)
    trainimg.append(img)
    trainlb.append(imgname[:9])

# convert the trainimg into array
trainimg = np.concatenate(trainimg)
# shuffling the data to get better results
from sklearn.utils import shuffle
trainimg,trainlb = shuffle(trainimg,trainlb)
# applying KNN
from sklearn import neighbors
model = neighbors.KNeighborsClassifier(n_neighbors=3)
model.fit(trainimg,trainlb)
#print the accurqacy on trian data
print("The accuracy on train data is ",model.score(trainimg,trainlb))

# save the model
from sklearn.externals import joblib
joblib.dump(model,"Face_model/facemodel.pkl")

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as im 
import cv2
#import images from folders 
face_folder1=r"Entry_picture"
face_folder2=r"Inside_picture2"
face_folder3=r"Exit_picture2"
file_names1 = os.listdir(face_folder1)
file_names2 = os.listdir(face_folder2)
file_names3 = os.listdir(face_folder3)
print("Entry pictures ", len(file_names1))
print("inside pictures ", len(file_names2))
print("Exit pictures ", len(file_names3))
#load_image  is a function that load the file, convert the image to  color gray , resize the image to 48by48 ,
#changing the image type to float , put it in array 
#the expand is to make channel first to channel last 
def load_image(folder,imgname):
    img=im.imread(folder+'//'+imgname)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(48,48))
    img=img.astype("float") / 255.0
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

 #import the model 
emotion_model_path = r"Emotion_model\_mini_XCEPTION.64-0.82.hdf5"
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["unhappy","happy","neutral"]

#get_mode_output is a function that accepts folder and filenames as parameter , defrentiate the names of images by spliting them,
# splitting the names of the images into 3 types (subject  entry time , and exit time) , predicts the emotion of each image respected to subject
# get the mode of the emotions and store it in csv file, and rename the the folder by the day date  ,with  the following columns: 
#index ,img subject, Entry emotion ,Entry time ,Inside emotions,Exit_emotions,Exit_time
#how to look at emotion :(0-2) 0=unhappy , 1=happy, 2=neutral)

def get_mode_output(folder,filenames):
    subject = []
    emotion = []
    time=[]
    groups = set([imgname.split("_")[1] for imgname in filenames])
    for group in groups:
        imgnames = [imgname for imgname in filenames if group in imgname]
        group_out=[]
        for imgname in imgnames:
            img = load_image(folder,imgname)
            pred = emotion_classifier.predict(img)[0]
            out = np.argmax(pred)
            group_out.append(EMOTIONS[out])
        subject.append(group)
        time.append(imgname.split('_')[-2])
        emotion.append(max(group_out,key = group_out.count))
    return subject,emotion,time


entry_img,entry_emo, entrytime = get_mode_output(face_folder1,file_names1)
inside_img,inside_emo, insidetime = get_mode_output(face_folder2, file_names2)
exit_img,exit_emo, exittime = get_mode_output(face_folder3, file_names3)        



df1=pd.DataFrame({"img":entry_img,"Entry_emotions":entry_emo,"Entry_time":entrytime})
df2=pd.DataFrame({"img":inside_img,"Inside_emotions":inside_emo})
df3=pd.DataFrame({"img":exit_img,"Exit_emotions":exit_emo,"Exit_time":exittime})
df1.set_index('img',inplace=True)
df2.set_index('img',inplace=True)
df3.set_index('img',inplace=True)
df = pd.concat([df1,df2,df3],axis=1,sort=False).reset_index()
df.rename(columns = {'index':'img'})

df.to_csv(r"output_data"+".".join(time.ctime().split(':'))+".csv")
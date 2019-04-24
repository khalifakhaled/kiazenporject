import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as im 
import cv2
import os 
import time

class capture_img:
    fd = cv2.CascadeClassifier("haarcascade_files\haarcascade_frontalface_alt.xml")
    j = 0
    def __init__(self,folder):
        self.folder = folder
        """
        the function accepts parameters [folder,]
        folder = the folder where you wish to save your images
        """
    def start_capture(self,delay=0.4,count=5,sf=1.3,interval = 0.1):
        """
        this function accepts the parameters - [delay,count,sf,interval]
        delay = the delay you wish to put between multiplt picutres clicked - the count of pictures will be according to value of count, default value = 0.4
        count = the number of pictures to be clicked, default value = 5
        sf = scaling factor, default value = 1.3
        interval = the time interval between two consecutive captures of images, default value = 0.1
        """
        self.vid = cv2.VideoCapture(0)
        while True:
            imgs=[]
            for i in range(count):
                ret,self.img = self.vid.read()
                time.sleep(delay)
                imgs.append(self.img)
            corners = self.fd.detectMultiScale(imgs[0],sf,2)
            for i in range(len(corners)):
                self.j=self.j+1
                (x,y,w,h)=corners[i]
                for i in range(len(imgs)):
                    face=imgs[i][y:y+w,x:x+h]
                    cv2.imwrite(self.folder+"\\"+"subject_"+str(self.j+1)+"_entry_"+str(i+1)+"_datetime_"+".".join(time.ctime().split(':'))+"_.jpg",face)
                cv2.rectangle(imgs[0],(x,y),(x+w,y+h),(0,0,255),1)
            cv2.imshow('img',imgs[0])
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
            time.sleep(interval)
        self.vid.release()
        cv2.destroyAllWindows()
    
    def load_image(self,imgname):
        """this function accept the imgname 
        loads the folder  and images , change there color to gray , reshaping the images to 1,10000 to array (flattening process ), 
        and return img and img2   """

        img=cv2.imread(self.folder+'//'+imgname)
        img2=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img2=cv2.resize(img2,(100,100))  
        img2 = img2.reshape(1,10000)
        return img,img2
       
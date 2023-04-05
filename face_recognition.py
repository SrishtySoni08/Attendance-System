from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime 
import cv2
import os
import numpy as np


class face_recognition:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1600x900+0+0")
    self.root.title("Face Recognition")

    
    title_lbl=Label(self.root,text="Face Recognition",font=("Algerian",40,"bold"),bg="black",fg="white")
    title_lbl.place(x=0,y=0,width=1600,height=60)

      #first image
    img=Image.open(r"Images\face6.jpg")
    img=img.resize((800,800),Image.ANTIALIAS)
    self.photoimg=ImageTk.PhotoImage(img)
                
    lbl=Label(self.root,image=self.photoimg) 
    lbl.place(x=0,y=60,width=800,height=760)
        #Second Image
    img1=Image.open(r"Images\face7.jpg")
    img1=img1.resize((1500,800),Image.ANTIALIAS)
    self.photoimg1=ImageTk.PhotoImage(img1)
                
    lbl=Label(self.root,image=self.photoimg1)
    lbl.place(x=800,y=60,width=800,height=760)  
        #button
    img2=Image.open(r"Images\face5.jpg")
    img2=img2.resize((400,500),Image.ANTIALIAS)
    self.photoimg5=ImageTk.PhotoImage(img2)

    b1=Button(self.root,command=self.face_recog,image=self.photoimg5,cursor="hand2")
    b1.place(x=570,y=150,width=400,height=500)

    b1_1=Button(self.root,command=self.face_recog,text="Start Scanning",cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
    b1_1.place(x=570,y=610,width=400,height=40)

        # bottom title
    bottom_lbl=Label(self.root,text="NO MORE PROXIES",font=("SEOGE SCRIPT",30,"bold"),bg="black",fg="white")
    bottom_lbl.place(x=0,y=820,width=1600,height=55)
     #===attendance====
  def mark_attendance(self,id,n,r,d):
      with open("Attendance.csv","r+",newline='\n') as f:
          myDataList=f.readlines()
          name_list=[]
          for line in myDataList:
            entry=line.split((","))
            name_list.append((entry[1]))
          if ((id not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
            now=datetime.now()
            d1=now.strftime("%d/%m/%y")
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f"{id},{r},{n},{d},{dtString},{d1},Present\n")
          
       
        #function
  def face_recog(self):
    def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        coord=[]
        for(x,y,w,h) in features:
          cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
          id,predict=clf.predict(gray_image[y:y+h,x:x+w])
          confidence=int((100*(1-predict/300)))
          

          

          if confidence>78:
                conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where StudentId={}".format(id))
                n=my_cursor.fetchone()
                n='+'.join(n)
          

                my_cursor.execute("Select RollNo from student where StudentId={}".format(id))
                r=my_cursor.fetchone()
                r='+'.join(r)

                my_cursor.execute("Select Dep from student where StudentId={}".format(id))
                d=my_cursor.fetchone()
                d='+'.join(d)

                cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
             
                self.mark_attendance(id,r,n,d)  
          else:
              cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
              cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
          coord=[x,y,w,h]
        return coord
    def recognize(img,clf,faceCascade):
        coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        return img

    faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read("Classifier.xml")

    video_cap=cv2.VideoCapture(0)

    while True:
        ret,img=video_cap.read()
        img=recognize(img,clf,faceCascade)
        cv2.imshow("Welcome to Face Recognition",img)

        if cv2.waitKey(1)==13:
            break
    video_cap.release()
    cv2.destroyAllWindows()




if __name__== "__main__":
    root=Tk()
    obj=face_recognition(root)  
    root.mainloop()
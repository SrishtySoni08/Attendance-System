from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1600x900+0+0")
    self.root.title(" Data Training")
    
    title_lbl=Label(self.root,text="Train Data Set",font=("Algerian",30,"bold"),bg="black",fg="white")
    title_lbl.place(x=0,y=0,width=1600,height=40)

     #First Image
    img=Image.open(r"Images\train2.jpg")
    img=img.resize((800,300),Image.ANTIALIAS)
    self.photoimg=ImageTk.PhotoImage(img)
                
    lbl=Label(self.root,image=self.photoimg)
    lbl.place(x=0,y=40,width=800,height=300)
      #Second Image
    img1=Image.open(r"Images\train3.jfif")
    img1=img1.resize((800,300),Image.ANTIALIAS)
    self.photoimg1=ImageTk.PhotoImage(img1)
                
    lbl=Label(self.root,image=self.photoimg1)
    lbl.place(x=801,y=40,width=800,height=300)

    
    img3=Image.open(r"Images\train1.jpg")
    img3=img3.resize((1600,600),Image.ANTIALIAS)
    self.photoimg2=ImageTk.PhotoImage(img3)
    
    bg_img=Label(self.root,image=self.photoimg2)
    bg_img.place(x=0,y=341,width=1600,height=560)

      # train button
    img4=Image.open(r"Images\train4.png")
    img4=img4.resize((500,400),Image.ANTIALIAS)
    self.photoimg3=ImageTk.PhotoImage(img4)

    b1=Button(bg_img,image=self.photoimg3,command=self.train_classifier,cursor="hand2")
    b1.place(x=450,y=50,width=500,height=400)
    b1_1=Button(bg_img,text="Train Data",command=self.train_classifier,cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
    b1_1.place(x=450,y=450,width=500,height=40)
    #function
  def train_classifier(self):
    data_dir=("Student Face Samples")
    path=[os.path.join(data_dir,files) for files in os.listdir(data_dir)]

    faces=[]
    ids=[]

    for image in path:
      img=Image.open(image).convert('L')
      imgNP=np.array(img,'uint8')
      id=int(os.path.split(image)[1].split('.')[1])
      print (id)
      faces.append(imgNP)
      ids.append(id)
      cv2.imshow('Training',imgNP)
      cv2.waitKey(1)==13
    ids=np.array(ids)
    
      #=== train classsifieer and save====
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("Classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("RESULT","Training Data Set is completed.")

    

    




if __name__== "__main__":
    root=Tk()
    obj=Train(root)  
    root.mainloop()




 
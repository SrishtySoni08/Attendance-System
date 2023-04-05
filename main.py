from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
import pyttsx3
from train import Train
from face_recognition import face_recognition
from attendance import Attendance
import pyaudio
import speech_recognition as sr
import pywhatkit
r=sr.Recognizer()
sr.Microphone()

voice_id = "Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        
converter = pyttsx3.init()
converter.setProperty('voice', voice_id)
converter.runAndWait()
pyttsx3.speak("hello user")

    
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recogniton System")
        #First Image
        img1=Image.open(r"Images\Poornima.jpg")
        img1=img1.resize((550,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl=Label(self.root,image=self.photoimg1)
        lbl.place(x=0,y=0,width=550,height=200)

        #Second Image
        img=Image.open(r"Images\face4.jpg")
        img=img.resize((500,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl=Label(self.root,image=self.photoimg)
        lbl.place(x=551,y=0,width=500,height=200)
        #Third Iamge
        img2=Image.open(r"Images\poornima3.jpg")
        img2=img2.resize((550,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl=Label(self.root,image=self.photoimg2)
        lbl.place(x=1051,y=0,width=550,height=200)
        #bg image
        img3=Image.open(r"Images\background1.jpg")
        img3=img3.resize((1600,745),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1600,height=750)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1600,height=55)
        
#microphone button
        img8=Image.open(r"Images\microphone.jpg")
        img8=img8.resize((50,50),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img8)

        microb=Button(bg_img,image=self.photoimg10,command=microphone,cursor="hand2")
        microb.place(x=20,y=0,width=50,height=50)
       
        # student button
        img4=Image.open(r"Images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
        b1_1.place(x=100,y=295,width=200,height=40)
        
        # Face detection button
        img5=Image.open(r"Images\face3.jpg")
        img5=img5.resize((300,300),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,command=self.Face_Recognition,image=self.photoimg5,cursor="hand2")
        b2.place(x=650,y=200,width=300,height=300)
        

        b2_1=Button(bg_img,command=self.Face_Recognition,text="Face Recognition",cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
        b2_1.place(x=650,y=495,width=300,height=40)

        # Attendance  button
        img6=Image.open(r"Images\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,command=self.Attendance,image=self.photoimg6,cursor="hand2")
        b3.place(x=100,y=400,width=200,height=200)

        b3_1=Button(bg_img,text="Attendance",command=self.Attendance,cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
        b3_1.place(x=100,y=595,width=200,height=40)

        #Train Button
        img7=Image.open(r"Images\train.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b4.place(x=1300,y=100,width=200,height=200)

        b4_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("Seoge script",20,"bold"),bg="black",fg="cyan")
        b4_1.place(x=1300,y=295,width=200,height=40)

        #Exit Button

        img8=Image.open(r"Images\exit.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,command=self.iexit,image=self.photoimg8,cursor="hand2")
        b5.place(x=1300,y=400,width=200,height=200)

        b5_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("Seoge script",20,"bold"),bg="black",fg="cyan")
        b5_1.place(x=1300,y=595,width=200,height=40)
    
    def iexit(self):
        self.iExit=messagebox.askyesno("Confirmation!","Are you sure to exit the face recognition system?")
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
     
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def Face_Recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)   

    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
def microphone():
        with sr.Microphone() as source:
            print("start say .... ")
            x=r.listen(source,timeout=3)
            p=r.recognize_google(x, language ='en')
            print(p)
            print("stop say ")
            bot_speaks(p)


def bot_speaks(p):
        uac = Face_Recognition_System(root)
        g='yes'
        print(p)
        while g=="yes":
            if("face recognition" in p):
                pyttsx3.speak("Opening Face Recognition Tab.")
                uac.Face_Recognition()
            elif("student Details" in p):
                pyttsx3.speak("Opening Student Details tab.")
                uac.student_details()
            elif("train data" in p):
                pyttsx3.speak("Opening train data tab.")
                uac.train_data()
            elif("attendance" in p):
                pyttsx3.speak("opening attendance tab.")
                uac.Attendance()
            elif("exit" or "close" or "end" in p):
                pyttsx3.speak("closing the facial recognition attendance system.")
                uac.iexit()
            else:
                pyttsx3.speak("I am unable to recognize the task.please,Command a valid task.")
            break


        

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
 



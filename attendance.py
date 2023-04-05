from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox

from cv2 import cv2
import csv
import os
from tkinter import filedialog

mydata=[]
class Attendance:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1600x900+0+0")
    self.root.title("Attendance System")

    self.var_dep=StringVar()
    self.var_std_id=StringVar()
    self.var_roll=StringVar()
    self.var_std_name=StringVar()
    self.var_attendance=StringVar()
    self.var_date=StringVar()
    self.var_time=StringVar()

    #first image
    img=Image.open(r"Images\attendance2.jpg")
    img=img.resize((800,300),Image.ANTIALIAS)
    self.photoimg=ImageTk.PhotoImage(img)
                
    lbl=Label(self.root,image=self.photoimg)
    lbl.place(x=0,y=0,width=800,height=300)
    #Second Image
    img1=Image.open(r"Images\attendance4.jpg")
    img1=img1.resize((800,300),Image.ANTIALIAS)
    self.photoimg1=ImageTk.PhotoImage(img1)

    lbl=Label(self.root,image=self.photoimg1)
    lbl.place(x=800,y=0,width=800,height=300) 
    #bg image
    img2=Image.open(r"Images\background1.jpg")
    img2=img2.resize((1600,600),Image.ANTIALIAS)
    self.photoimg3=ImageTk.PhotoImage(img2)
                
    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=300,width=1600,height=600)
    
    title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",30,"bold"),bg="black",fg="white")
    title_lbl.place(x=0,y=0,width=1600,height=45)

    main_frame=Frame(bg_img,bd=2,bg='paleturquoise')
    main_frame.place(x=20,y=48,width=1560,height=500)

    #left  label frame
    left_frame=LabelFrame(main_frame,bd=2,bg='black',relief=RAISED,text='Attendance Details',font=('times new roman',12,'bold'),fg='white')
    left_frame.place(x=10,y=5,width=750,height=490)

    img4=Image.open(r"Images\attendance3.jpeg")
    img4=img4.resize((750,130),Image.ANTIALIAS)
    self.photoimg4=ImageTk.PhotoImage(img4)
                
    lbl1=Label(left_frame,image=self.photoimg4)
    lbl1.place(x=5,y=0,width=730,height=130)
    
    left_inside=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
    left_inside.place(x=0,y=135,width=750,height=300)

    #===label and entry======
    #attendanceid
    StudentID_lbl=Label(left_inside,text="Student ID:",bg="white",font=('times new roman',12,'bold'))
    StudentID_lbl.grid(row=0,column=0,padx=10,pady=5)

    StudentID_entry=ttk.Entry(left_inside,textvariable=self.var_std_id,width=20,font=('comicsansns',13,'bold'),state='readonly')
    StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #roll
    roll_lbl=Label(left_inside,text="Roll No:",bg="white",font=('times new roman',12,'bold'))
    roll_lbl.grid(row=0,column=2,padx=10,pady=5)

    roll_entry=ttk.Entry(left_inside,width=20,textvariable=self.var_roll,font=('comicsansns',13,'bold'),state='readonly')
    roll_entry.grid(row=0,column=3,pady=5)

    #name
    name_lbl=Label(left_inside,text="Name:",bg="white",font=('times new roman',12,'bold'))
    name_lbl.grid(row=1,column=0)

    name_entry=ttk.Entry(left_inside,textvariable=self.var_std_name,width=20,font=('comicsansns',13,'bold'))
    name_entry.grid(row=1,column=1,pady=8)
    
    #Department
    dep_lbl=Label(left_inside,text="Department:",bg="white",font=('times new roman',12,'bold'))
    dep_lbl.grid(row=1,column=2)

    dep_entry=ttk.Entry(left_inside,textvariable=self.var_dep,width=20,font=('comicsansns',13,'bold'))
    dep_entry.grid(row=1,column=3,pady=8)
    
    #date
    date_lbl=Label(left_inside,text="Date:",bg="white",font=('times new roman',12,'bold'))
    date_lbl.grid(row=2,column=0,padx=10,pady=5)

    date_entry=ttk.Entry(left_inside,width=20,textvariable=self.var_date,font=('comicsansns',13,'bold'))
    date_entry.grid(row=2,column=1,pady=5)
 
    #time
    time_lbl=Label(left_inside,text="Time:",bg="white",font=('times new roman',12,'bold'))
    time_lbl.grid(row=2,column=2)

    time_entry=ttk.Entry(left_inside,width=20,textvariable=self.var_time,font=('comicsansns',13,'bold'))
    time_entry.grid(row=2,column=3,pady=8)
    
    #attendance
    attendance_lbl=Label(left_inside,text="Attendance:",bg="white",font=('times new roman',12,'bold'))
    attendance_lbl.grid(row=3,column=0)

    self.atten_status=ttk.Combobox(left_inside,textvariable=self.var_attendance,width=20,font=('comicsansns',11,'bold'),state='readonly')
    self.atten_status["values"]=("Select Status","Present","Absent")
    self.atten_status.grid(row=3,column=1,pady=8)
    self.atten_status.current(0)
    #Button Frame
    btn_frame=Frame(left_inside,bd=2,relief=RIDGE,bg='white')
    btn_frame.place(x=0,y=200,width=745,height=42)

    import_btn=Button(btn_frame,text='Import CSV',width=16,command=self.importCSV,font=('times new roman',14,'bold'),bg='blue',fg='black')
    import_btn.grid(row=0,column=0)

    export_btn=Button(btn_frame,text='Export CSV',width=16,command=self.exportCSV,font=('times new roman',14,'bold'),bg='blue',fg='black')
    export_btn.grid(row=0,column=1)

    update_btn=Button(btn_frame,text='Update',width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
    update_btn.grid(row=0,column=2)

    reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
    reset_btn.grid(row=0,column=3)


    #right label frame
    right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RAISED,text='Student Details',font=('times new roman',12,'bold'))
    right_frame.place(x=780,y=5,width=760,height=490)
                
    img5=Image.open(r"Images\clg.jpg")
    img5=img5.resize((750,130),Image.ANTIALIAS)
    self.photoimg5=ImageTk.PhotoImage(img5)
                
    lbl2=Label(right_frame,image=self.photoimg5)
    lbl2.place(x=5,y=0,width=730,height=130)

    #Table frame
    table_frame=Frame(right_frame,bd=2,bg='white',relief=SUNKEN)
    table_frame.place(x=5,y=135,width=730,height=330)
                
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    
    self.AttendanceReportTable=ttk.Treeview(table_frame,column=('id','name','roll','dep','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)    
    scroll_x.config(command=self.AttendanceReportTable.xview)
    scroll_y.config(command=self.AttendanceReportTable.yview)
    
    self.AttendanceReportTable.heading("id",text="StudentID")
    self.AttendanceReportTable.heading("name",text="Name")
    self.AttendanceReportTable.heading("roll",text="RollNo")
    self.AttendanceReportTable.heading("dep",text="Department")
    self.AttendanceReportTable.heading("date",text="Date")
    self.AttendanceReportTable.heading("time",text="Time") 
    self.AttendanceReportTable.heading("attendance",text="Attendance")
    
    self.AttendanceReportTable["show"]="headings"

    self.AttendanceReportTable.column("dep",width=100)
    self.AttendanceReportTable.column("id",width=100)
    self.AttendanceReportTable.column("name",width=100)
    self.AttendanceReportTable.column("roll",width=100)
    self.AttendanceReportTable.column("date",width=100)
    self.AttendanceReportTable.column("time",width=100)
    self.AttendanceReportTable.column("attendance",width=150)

    self.AttendanceReportTable.pack(fill=BOTH,expand=1)
    self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #====fetch data====
  def fetchData(self,rows):
    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
    for i in rows:
      self.AttendanceReportTable.insert("",END,values=i)
  
  def importCSV(self):
    global mydata
    mydata.clear()
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*csv"),("All File","*.*")),parent=self.root)
    with open(fln) as myfile:
      csvread=csv.reader(myfile,delimiter=",")
      for i in csvread:
        mydata.append(i)
      self.fetchData(mydata)

  def exportCSV(self):
    try:
      if len(mydata)<1:
        messagebox.showerror("No DATA!","No data found to export.",parent=self.root)
        return False
      fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*csv"),("All File","*.*")),parent=self.root)    
      with open(fln,mode='w',newline="") as myfile:
        exp_write=csv.writer(myfile,delimiter=",")
        for i in mydata:
          exp_write.writerow(i)
        messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(fln)+" successfully.",parent=self.root)
    except Exception as es:
      messagebox.showerror("ERROR!",f"Due to:{str(es)}",parent=self.root)
#=========set data==========
  def get_cursor(self,event=""):
    cursor_focus=self.AttendanceReportTable.focus()
    content=self.AttendanceReportTable.item(cursor_focus)
    data=content["values"]

    self.var_std_id.set(data[0])
    self.var_std_name.set(data[1])
    self.var_roll.set(data[2])
    self.var_dep.set(data[3])
    self.var_time.set(data[4])
    self.var_date.set(data[5])
    self.var_attendance.set(data[6])
    #reset data
  def reset_data(self):  
    self.var_std_id.set("")
    self.var_std_name.set("")
    self.var_roll.set("")
    self.var_dep.set("")
    self.var_time.set("")
    self.var_date.set("")
    self.var_attendance.set("")
 

    

if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)  
    root.mainloop()
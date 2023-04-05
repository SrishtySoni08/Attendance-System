from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2



class Student:
  def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Student Details")
         #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_search=StringVar()
        self.var_combo=StringVar()
        

        #First Image
        img=Image.open(r"Images\face1.jpg")
        img=img.resize((450,180),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
                
        lbl=Label(self.root,image=self.photoimg)
        lbl.place(x=0,y=0,width=450,height=180)
        #Second Image
        img1=Image.open(r"Images\Poornima.jpg")
        img1=img1.resize((800,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
                
        lbl=Label(self.root,image=self.photoimg1)
        lbl.place(x=451,y=0,width=750,height=180)
        #Third Iamge
        img2=Image.open(r"Images\face2.jpg")
        img2=img2.resize((400,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
                
        lbl=Label(self.root,image=self.photoimg2)
        lbl.place(x=1202,y=0,width=400,height=180)
        #        bg image
        img3=Image.open(r"Images\background1.jpg")
        img3=img3.resize((1600,745),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
                
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=180,width=1600,height=750)

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1600,height=40)

        main_frame=Frame(bg_img,bd=2,bg='paleturquoise')
        main_frame.place(x=20,y=45,width=1600,height=665)

        #left  label frame
        left_frame=LabelFrame(main_frame,bd=2,bg='black',relief=RAISED,text='Student Details',font=('times new roman',12,'bold'),fg='white')
        left_frame.place(x=5,y=5,width=770,height=625)

        img4=Image.open(r"Images\Poornima.jpg")
        img4=img4.resize((760,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
                
        lbl1=Label(left_frame,image=self.photoimg4)
        lbl1.place(x=5,y=0,width=758,height=190)

        #course frame
        course=LabelFrame(left_frame,bd=2,bg='white',relief=SUNKEN,text='Course Information',font=('times new roman',12,'bold'))
        course.place(x=5,y=192,width=758,height=90)

        #Department 
        Department=Label(course,text='Department',font=('times new roman',12,'bold'),bg='white')
        Department.grid(row=0,column=0,padx=50)

        dep=ttk.Combobox(course,font=('times new roman',12,'bold'),textvariable=self.var_dep,state='readonly')
        dep['values']=('Select Department','Computer Science','Artificial Intelligence','Mechanical','Civil','Electrical')
        dep.current(0)  
        dep.grid(row=0,column=1,padx=2,pady=5)

        #Course
        course_label=Label(course,text='Course',bg='white',font=('times new roman',12,'bold'))
        course_label.grid(row=0,column=2,padx=50)

        Course=ttk.Combobox(course,textvariable=self.var_course,font=('times new roman',12,'bold'),state='readonly')
        Course['values']=('Select Course','B.Tech','BCA','','','')
        Course.current(0)  
        Course.grid(row=0,column=3,padx=2,pady=5)

        #Year
        year_label=Label(course,text='Year',bg='white',font=('times new roman',12,'bold'))
        year_label.grid(row=1,column=0,padx=50)
        year=ttk.Combobox(course,textvariable=self.var_year,font=('times new roman',12,'bold'),state='readonly')
        year['values']=('Select Year','I','II','III','IV')
        year.current(0)  
        year.grid(row=1,column=1,padx=2,pady=5)

        #Semester
        sem_label=Label(course,text='Semester',bg='white',font=('times new roman',12,'bold'))
        sem_label.grid(row=1,column=2,padx=50)

        sem=ttk.Combobox(course,textvariable=self.var_semester,font=('times new roman',12,'bold'),state='readonly')
        sem['values']=('Select Semester','I','II')
        sem.current(0)  
        sem.grid(row=1,column=3,padx=2,pady=5)

        #Student info frame
        student_info=LabelFrame(left_frame,bd=2,bg='white',relief=SUNKEN,text='Student Details',font=('times new roman',12,'bold'))
        student_info.place(x=5,y=285,width=758,height=310)
        #Student Id 
        id=Label(student_info,text='Student Id:',font=('times new roman',12,'bold'),bg='white')
        id.grid(row=0,column=0,padx=5)

        id_entry=ttk.Entry(student_info,textvariable=self.var_std_id,width=20,font=('times new roman',12,'bold'))
        id_entry.grid(row=0,column=1,padx=5,pady=10)
       #Student Name 
        Name=Label(student_info,text='Student Name:',font=('times new roman',12,'bold'),bg='white')
        Name.grid(row=0,column=2,padx=5)

        name_entry=ttk.Entry(student_info,textvariable=self.var_std_name,width=20,font=('times new roman',12,'bold'))
        name_entry.grid(row=0,column=3,padx=5,pady=10)
        #Section 
        Section=Label(student_info,text='Section:',font=('times new roman',12,'bold'),bg='white')
        Section.grid(row=1,column=0,padx=5)

        sec_entry=ttk.Combobox(student_info,textvariable=self.var_section,width=20,font=('times new roman',12,'bold'),state='readonly')
        sec_entry['values']=('Select Section','A','B',)
        sec_entry.current(0)
        sec_entry.grid(row=1,column=1,padx=5,pady=10)
        #Roll no 
        RollNo=Label(student_info,text='Roll No:',font=('times new roman',12,'bold'),bg='white')
        RollNo.grid(row=1,column=2,padx=5)

        rollno_entry=ttk.Entry(student_info,textvariable=self.var_roll,width=20,font=('times new roman',12,'bold'))
        rollno_entry.grid(row=1,column=3,padx=5,pady=10)
        #Gender 
        gender=Label(student_info,text='Gender:',font=('times new roman',12,'bold'),bg='white')
        gender.grid(row=2,column=0,padx=5)

        gender_entry=ttk.Combobox(student_info,textvariable=self.var_gender,width=20,font=('times new roman',12,'bold'),state='readonly')
        gender_entry['values']=('Select Gender','Male','Female','Others')
        gender_entry.current(0)
        gender_entry.grid(row=2,column=1,padx=5,pady=10,)
        #Phone No        
        PhoneNo=Label(student_info,text='Phone No:',font=('times new roman',12,'bold'),bg='white')
        PhoneNo.grid(row=2,column=2,padx=5)

        PhoneNo_entry=ttk.Entry(student_info,textvariable=self.var_phone,width=20,font=('times new roman',12,'bold'))
        PhoneNo_entry.grid(row=2,column=3,padx=5,pady=10)
        #radio buttons
        self.var_radio1=StringVar()
        rd1=ttk.Radiobutton(student_info,variable=self.var_radio1,text='Add Face Sample',value='Available')
        rd1.grid(row=3,column=0,padx=5,pady=10)
                
        rd2=ttk.Radiobutton(student_info,variable=self.var_radio1,text='Continue Without Face Sample',value='Unavailable')
        rd2.grid(row=3,column=1,padx=5,pady=10)     
        #Button Frame
        btn_frame=Frame(student_info,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=745,height=42)

        save_btn=Button(btn_frame,command=self.add_data,text='Save',width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text='Update',command=self.update_data,width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text='Delete',command=self.delete_data,width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_entries,width=16,font=('times new roman',14,'bold'),bg='blue',fg='black')
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(student_info,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=242,width=745,height=42)
                
        

        update_photo_btn=Button(btn_frame1,text='Update Face',command=self.capture,width=33,font=('times new roman',14,'bold'),bg='blue',fg='black')
        update_photo_btn.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RAISED,text='Student Details',font=('times new roman',12,'bold'))
        right_frame.place(x=790,y=5,width=770,height=635)
                
        img5=Image.open(r"Images\Poornima.jpg")
        img5=img5.resize((760,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
                
        lbl2=Label(right_frame,image=self.photoimg5)
        lbl2.place(x=5,y=0,width=758,height=190)
        #Search Frame
        search_frame=LabelFrame(right_frame,bd=2,bg='white',relief=SUNKEN,text='Search System',font=('times new roman',12,'bold'))
        search_frame.place(x=5,y=192,width=758,height=65)

        search_label=Label(search_frame,text='Search by:',font=('times new roman',15,'bold'),bg='violet',fg='black')
        search_label.grid(row=0,column=0)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo,width=10,font=('times new roman',13),state='readonly')
        search_combo['values']=('Select type','RollNo','MobileNo')
        search_combo.current(0)  
        search_combo.grid(row=0,column=1,padx=20,pady=5)

        Search_entry=ttk.Entry(search_frame,width=25,textvariable=self.var_search,font=('times new roman',12,'bold'))
        Search_entry.grid(row=0,column=2,padx=20,pady=10,)

        search_btn=Button(search_frame,text='Search',command=self.search,width=14,font=('times new roman',12,'bold'),bg='blue',fg='black')
        search_btn.grid(row=0,column=3)

        ShowAll_btn=Button(search_frame,command=self.fetch_data,text='Show All',width=14,font=('times new roman',12,'bold'),bg='blue',fg='black')
        ShowAll_btn.grid(row=0,column=4)
        #Table frame
        table_frame=Frame(right_frame,bd=2,bg='white',relief=SUNKEN)
        table_frame.place(x=5,y=260,width=758,height=350)
                
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=('id','name','roll','dep','course','sec','year','sem','gender','phone','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("sec",text="Section") 
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")            
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="MobileNo")
        self.student_table.heading("photo",text="FaceSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()              
        
#=========Function declaration
  def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"\
        or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_section.get()=="Select Section"\
        or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_radio1.get()=="":
                messagebox.showerror("Error!","All fields are required.")
        else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_section.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_radio1.get()     
                    ))   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully.",parent=self.root)
                if self.var_radio1.get()=="Available":
                  self.capture()
                else:
                  pass              
             except Exception as es:
                messagebox.showerror("Error!",f"Due to:{str(es)}",parent=self.root)
          
    
#=========fetch data===========
  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from student")
    data=my_cursor.fetchall()
        
    if len(data)!=0:
      self.student_table.delete(*self.student_table.get_children())
      for i in data:
        self.student_table.insert("",END,values=i)
      conn.commit()
    conn.close()
#=========set data==========
  def get_cursor(self,event=""):
    cursor_focus=self.student_table.focus()
    content=self.student_table.item(cursor_focus)
    data=content["values"]

    self.var_std_id.set(data[0])
    self.var_std_name.set(data[1])
    self.var_roll.set(data[2])
    self.var_dep.set(data[3])
    self.var_course.set(data[4])
    self.var_section.set(data[5])
    self.var_year.set(data[6])
    self.var_semester.set(data[7])
    self.var_gender.set(data[8])
    self.var_phone.set(data[9])
    self.var_radio1.set(data[10])
    # update function
  def update_data(self):
    if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"\
       or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_section.get()=="Select Section"\
       or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_radio1.get()=="":
       messagebox.showerror("Error!","All fields are required.",parent=self.root)
    else:
      try:
        Update=messagebox.askyesno("Update Confirmation","Do you want to update the details for this student?",parent=self.root)
        if Update>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
          my_cursor=conn.cursor()
          my_cursor.execute("Update student set Name=%s,RollNo=%s,Dep=%s,Course=%s,Section=%s,Year=%s,Semester=%s,Gender=%s,MobileNo=%s,FaceSampleStatus=%s where StudentId=%s",(
                self.var_std_name.get(),
                self.var_roll.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_section.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_gender.get(),
                self.var_phone.get(),
                self.var_radio1.get(), 
                self.var_std_id.get()
                ))
        else:
          if not Update:
            return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Student details has been updated.",parent=self.root)
      except Exception as es:
        messagebox.showerror("ERROR!",f"Due to:{str(es)}",parent=self.root)
    #delete function
  def delete_data(self):
    if self.var_std_id.get()=="":
      messagebox.showerror("ERROR!","Student ID is required.",parent=self.root)    
    else:
      try:
        delete=messagebox.askyesno("Delete Confirmation","Do you want to delete the details of this student completely?",parent=self.root)
        if delete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
          my_cursor=conn.cursor()
          sql="delete from student where StudentId=%s"
          val=(self.var_std_id.get(),)
          my_cursor.execute(sql,val)
        else:
          if not delete:
            return
        conn.commit()
        self.fetch_data()
        self.reset_entries()
        conn.close()
        messagebox.showinfo("SUCCESS","Details of the student has been deleted.",parent=self.root)     
      except Exception as es:
         messagebox.showerror("ERROR!",f"Due to:{str(es)}",parent=self.root)
         #reset function
  def reset_entries(self):
    self.var_course.set("Select Course")
    self.var_dep.set("Select Department")
    self.var_year.set("Select Year")
    self.var_semester.set("Select Semester")
    self.var_section.set("Select Section")
    self.var_std_id.set("")
    self.var_std_name.set("")
    self.var_roll.set("")
    self.var_gender.set("Select Gender")
    self.var_phone.set("")
    self.var_radio1.set("")

      #Face samples
  def capture(self):
    if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_section.get()=="Select Section" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_radio1.get()=="":
      messagebox.showerror("Error!","All fields are required.",parent=self.root)
    elif self.var_radio1.get()=="Unavailable":
      messagebox.showerror("ERROR!","You have to choose the correct option:'Add face sample'",parent=self.root )
    else:
      try:
        conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        myresult=my_cursor.fetchall()
        id=self.var_std_id.get()
        
        my_cursor.execute("Update student set Name=%s,RollNo=%s,Dep=%s,Course=%s,Section=%s,Year=%s,Semester=%s,Gender=%s,MobileNo=%s,FaceSampleStatus=%s where StudentId=%s",(
                self.var_std_name.get(),
                self.var_roll.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_section.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_gender.get(),
                self.var_phone.get(),
                self.var_radio1.get(), 
                self.var_std_id.get()==id
                ))
        conn.commit()
        self.fetch_data()
        self.reset_entries()
        conn.close()
      

         #======load  predefined data on face frontalsfrom opencv======
        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
          gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          faces=face_classifier.detectMultiScale(gray,1.3,5)

          for(x,y,w,h) in faces:
            face_cropped=img[y:y+h,x:x+w]
            return face_cropped
        cap=cv2.VideoCapture(0)
        img_id=0
        while True:
          ret,my_frame=cap.read()
          if face_cropped(my_frame) is not None:
            img_id+=1
            face=cv2.resize(face_cropped(my_frame),(450,450))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path=("Student Face Samples/user."+str(id)+"."+str(img_id)+".jpg")
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
            cv2.imshow("Capturing Face",face)

          if cv2.waitKey(1)==13 or int(img_id)==100:
            break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Generating data sets completed!!")
      except Exception as es:
        messagebox.showerror("ERROR!",f"Due to:{str(es)}",parent=self.root)
  
  def search(self):
    if self.var_search.get()=="" or self.var_combo.get()=="Select type":
      messagebox.showerror("ERROR!","Select Data type and enter the data accordingly.",parent=self.root)
    else:
      conn=mysql.connector.connect(host="localhost",username="root",password="vvss2418",database="attendance_management")
      my_cursor=conn.cursor()       
      my_cursor.execute("select * from student where "+str(self.var_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'") 
      data=my_cursor.fetchall()
        
      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
      conn.close()


                        


if __name__== "__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()
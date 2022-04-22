from tkinter import *
from tkinter import messagebox
import datetime
#import smslogin_form


import os
import mysql.connector
################ LOCAL HOST MYSQL DATABASE CONNECTION #########################
'''mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='' #put password of local database,
    database='' #database used
    )'''

################ CLEVER CLOUD SERVER MYSQL DATABASE CONNECTION #########################
try:
    mydb=mysql.connector.connect(
        host='b34hlxjqjbpnwinxud9w-mysql.services.clever-cloud.com',
        user='u6haifwrupocxuc7',
        password='zYNz****rXti****gOaT8', #password of clever cloud mysql
        database='************'      #database made on clever cloud used
        )


    mc=mydb.cursor()

except:
    messagebox.showinfo('Connectivity Problem','Internet Issue\nor\nDatabase does not exixts')

else:


    class sms():
        def __init__(self,root,username,actor):
            self.actor=actor
            self.username=username
            self.root=root
            self.root.title('STUDENT MANAGEMENT SYSTEM')
            self.root.geometry('1325x710+10+10')
            self.root.resizable(0,0)
            self.root.iconbitmap('smslogo.ico')
            self.root.configure(background='lightblue')

            #******************** DETAILS VARIABLES ******************

            self.year=StringVar()
            self.first_name=StringVar()
            self.middle_name=StringVar()
            self.last_name=StringVar()
            self.student_no=StringVar()
            self.dob=StringVar()
            self.mob_no=StringVar()
            self.course=StringVar()
            self.branch=StringVar()
            self.gender=StringVar()
            self.blood_group=StringVar()
            self.father_name=StringVar()
            self.mother_name=StringVar()
            self.email=StringVar()
            self.address=StringVar()


            #********************* MARKS VARIABLES *******************

            self.exam_type=StringVar()
            self.mark1=StringVar()
            self.mark2=StringVar()
            self.mark3=StringVar()
            self.mark4=StringVar()
            self.mark5=StringVar()
            self.mark6=StringVar()
            self.branch2=StringVar()


            self.marksbranch=StringVar()

            self.branchadd=StringVar()



            #******************display variables *********************
            self.name1=StringVar()
            self.student1_no=StringVar()
            self.dob1=StringVar()
            self.mob1_no=StringVar()
            self.course1=StringVar()
            self.branch1=StringVar()
            self.gender1=StringVar()
            self.blood1_group=StringVar()
            self.father1_name=StringVar()
            self.mother1_name=StringVar()
            self.email1=StringVar()
            self.address1=StringVar()

            self.modify_flag=0

            
            self.mainpage()

        def back_1(self):
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()

            self.title2.destroy()
            self.mainpage()

        def back(self):
            self.frame2.destroy()
            self.backbutton.destroy()
            self.title2.destroy()
            if self.actor=='stu':
                self.exitbutton.destroy()
            self.mainpage()
            
        def back_2_studentdetails(self):
            self.frame2.destroy()
            self.backbutton.destroy()
            self.exitbutton.destroy()
            self.title2.destroy()
            self.studentdetails_page(self.year.get())


        def back_2_studentmarks(self):
            self.frame2.destroy()
            self.backbutton.destroy()
            self.exitbutton.destroy()
            self.title2.destroy()
            self.studentmarks_page(self.year.get())

        def exit(self):
            op1=messagebox.askyesno('Aert!','Do you want to Save your Data')
            if op1>0:
                self.save()
                self.exitmainpage()
            else:
                self.exitmainpage()


        def clear_marks(self):
            self.frame3.destroy()
            self.stdno_entry.config(state="normal")
            self.student_no.set('')
            self.stdno_entry.focus()
            self.exam_type.set("Select Exam Type")



        def clear_search_marks(self):

            self.stno_entry.config(state='normal')
            self.student1_no.set('')
            self.stno_entry.focus()
            self.name1.set('')
            self.marksbranch.set('')

            self.framemarks.destroy()

            self.framemarks=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.framemarks.place(x=250,y=190,width=830,height=450)




            

                

        def clear(self):
            self.student_no.set('')
            self.first_name.set('')
            self.middle_name.set('')
            self.last_name.set('')
            self.father_name.set('')
            self.mother_name.set('')
            self.course.set('')
            self.branch.set('')
            self.dob.set('')
            self.mob_no.set('')
            self.gender.set('')
            self.email.set('')
            self.blood_group.set('')



    #*********************************MAIN PAGE ************************************************************************************

        def logout_page(self):
            self.root.destroy()
            

        def mainpage(self):
            #************************** MAIN PAGE ************************

            self.title1=Label(self.root,text='{} STUDENT MANAGEMENT SYSTEM {}'.format('='*35,'='*35),font=('arial',20,'bold'),bg='blue',fg='white',bd=5,relief=RAISED,pady=7)
            self.title1.pack(fill=X,pady=3)


            self.frame1=Frame(self.root,bg='blue',width=100,bd=5,relief=GROOVE)
            self.frame1.place(x=20,y=90,width=1285,height=570)

            logout=Button(self.frame1,text='Logout',activebackground='black',activeforeground='yellow',bg='red',command=self.logout_page,relief=FLAT,font=("bookman",12,"bold")).place(x=1202,y=1)


            if self.actor=='stu':
                button1=Button(self.frame1,text="STUDENT DETAILS ",activebackground='black',activeforeground='yellow',width=40,height=9,bg='lightblue',command=self.year_details_page,bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=120,pady=150)
                button2=Button(self.frame1,text="STUDENT MARKS ",activebackground='black',activeforeground='yellow',width=40,height=9,fg='BLACK',bg='lightblue',command=self.year_marks_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=80,pady=150)
            else:
                button1=Button(self.frame1,text="STUDENT DETAILS SYSTEM",activebackground='black',activeforeground='yellow',width=40,height=9,bg='lightblue',command=self.year_details_page,bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=120,pady=150)
                button2=Button(self.frame1,text="STUDENT MARKS SYSTEM",activebackground='black',activeforeground='yellow',width=40,height=9,fg='BLACK',bg='lightblue',command=self.year_marks_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=80,pady=150)
            credit=Label(self.root,text='© Copyright 2020. All Rights Reserved. VG Softwares pvt ltd.',fg='black',bg='lightblue',font=('Arial Rounded MT Bold',12)).place(x=430,y=670)

            

    #*********************************YEAR FOR STUDENT DETAILS PAGE ************************************************************************************

            

        def year_details_page(self):
            self.title1.destroy()
            self.frame1.destroy()

            if self.actor == 'stu':
                self.student1_no.set(self.username)
                
                self.searchstudent_page()
                

            else:

                self.title2=Label(self.root,text='CHOOSE YEAR',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.frame2=Frame(self.root,bg='blue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)

                Button(self.frame2,text="1st Year",activebackground='black',activeforeground='yellow',width=30,height=7,bg='lightblue',command=lambda:self.studentdetails_page('I'),bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=200,pady=60)
                Button(self.frame2,text="2nd Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentdetails_page('II'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=50,pady=60)
                Button(self.frame2,text="3rd Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentdetails_page('III'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=0,padx=60,pady=60)
                Button(self.frame2,text="4th Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentdetails_page('IV'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=1,padx=50,pady=60)
                



    #********************************* YEAR FOR STUDENT MARKS PAGE ************************************************************************************




        def year_marks_page(self):
            self.title1.destroy()
            self.frame1.destroy()

            if self.actor == 'stu':
                self.student1_no.set(self.username)
                year_formula=('SELECT year FROM student WHERE Student_no=%s')
                mc.execute(year_formula,(eval(self.student1_no.get()),))

                for y in mc:
                    pass
                self.year.set(y[0])
                self.searchmarks_page()


            else:
                self.title2=Label(self.root,text='CHOOSE YEAR',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.frame2=Frame(self.root,bg='blue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)

                Button(self.frame2,text="1st Year",activebackground='black',activeforeground='yellow',width=30,height=7,bg='lightblue',command=lambda:self.studentmarks_page('I'),bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=200,pady=60)
                Button(self.frame2,text="2nd Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentmarks_page('II'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=50,pady=60)
                Button(self.frame2,text="3rd Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentmarks_page('III'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=0,padx=60,pady=60)
                Button(self.frame2,text="4th Year",activebackground='black',activeforeground='yellow',width=30,height=7,fg='BLACK',bg='lightblue',command=lambda:self.studentmarks_page('IV'),bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=1,padx=50,pady=60)




    #*********************************STUDENT MARKS PAGE ************************************************************************************


        def studentmarks_page(self,year):

            self.title1.destroy()
            self.frame1.destroy()
            self.frame2.destroy()
            self.title2.destroy()
            self.backbutton.destroy()

            self.year.set(year)

            self.title2=Label(self.root,text='{} STUDENTS MARKS SYSTEM {}'.format('='*35,'='*35),font=('arial',20,'bold'),bg='blue',fg='white',bd=5,relief=RAISED,pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton1=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_1,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.backbutton1.place(x=20,y=59)

            self.exitbutton1=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.exitbutton1.place(x=1247,y=59)


            self.frame11=Frame(self.root,bg='blue',width=100,bd=5,relief=GROOVE)
            self.frame11.place(x=20,y=90,width=1285,height=570)

            Label(self.frame11,text='{} YEAR'.format(year),bg='blue',fg='yellow',bd=0,relief=SOLID,font=('arial',16,'bold')).place(x=590,y=10)
            
            button1=Button(self.frame11,text="ADD STUDENT MARKS",activebackground='black',activeforeground='yellow',width=25,height=7,bg='lightblue',command=self.addmarks_page,bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=220,pady=50)
            button2=Button(self.frame11,text="SEARCH STUDENT MARKS",activebackground='black',activeforeground='yellow',width=25,height=7,fg='BLACK',bg='lightblue',command=self.searchmarks_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=80,pady=50)
            button3=Button(self.frame11,text="MODIFY STUDENT MARKS",activebackground='black',activeforeground='yellow',width=25,height=7,fg='BLACK',bg='lightblue',command=self.modifymarks_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=0,padx=80,pady=50)
            button4=Button(self.frame11,text="EXIT",activebackground='black',activeforeground='yellow',width=25,height=7,fg='BLACK',bg='lightblue',command=self.exitmainpage,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=1,padx=60,pady=50)


            

    #*********************************STUDENT DETAILS PAGE ************************************************************************************



        def studentdetails_page(self,year):
            self.title1.destroy()
            self.frame1.destroy()
            self.frame2.destroy()
            self.title2.destroy()
            self.backbutton.destroy()

            self.year.set(year)

            self.title2=Label(self.root,text='{} STUDENTS DETAILS SYSTEM {}'.format('='*35,'='*35),font=('arial',20,'bold'),bg='blue',fg='white',bd=5,relief=RAISED,pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton1=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_1,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.backbutton1.place(x=20,y=59)

            self.exitbutton1=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.exitbutton1.place(x=1247,y=59)


            self.frame11=Frame(self.root,bg='blue',width=100,bd=5,relief=GROOVE)
            self.frame11.place(x=20,y=90,width=1285,height=570)

            Label(self.frame11,text='{} YEAR'.format(year),bg='blue',fg='yellow',bd=0,relief=SOLID,font=('arial',16,'bold')).place(x=590,y=10)
            
            button1=Button(self.frame11,text="ADD STUDENT",activebackground='black',activeforeground='yellow',width=20,height=7,bg='lightblue',command=self.addstudent_page,bd=6,relief=RAISED,font=("bookman",12,"bold")).grid(row=0,column=0,padx=52,pady=60)
            button2=Button(self.frame11,text="SEARCH STUDENT",activebackground='black',activeforeground='yellow',width=20,height=7,fg='BLACK',bg='lightblue',command=self.searchstudent_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=1,padx=40,pady=60)
            button3=Button(self.frame11,text="UPDATE STUDENT",activebackground='black',activeforeground='yellow',width=20,height=7,fg='BLACK',bg='lightblue',command=self.updatestudent_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=2,padx=60,pady=60)
            button4=Button(self.frame11,text="DISPLAY STUDENT",activebackground='black',activeforeground='yellow',width=20,height=7,fg='BLACK',bg='lightblue',command=self.displaystudent_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=0,column=3,padx=40,pady=60)
            button5=Button(self.frame11,text="DELETE STUDENT",activebackground='black',activeforeground='yellow',width=20,height=7,bg='lightblue',command=self.deletestudent_page,relief='raised',bd=6,font=("bookman",12,"bold")).grid(row=1,column=0,padx=52,pady=60)
            button6=Button(self.frame11,text="STUDENT ATTENDENCE",activebackground='black',activeforeground='yellow',width=20,height=7,fg='BLACK',bg='lightblue',command=self.studentattendance_page,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=1,padx=40,pady=60)
            button7=Button(self.frame11,text="EXIT",activebackground='black',activeforeground='yellow',width=20,height=7,fg='BLACK',bg='lightblue',command=self.exitmainpage,bd=6,relief='raised',font=("bookman",12,"bold")).grid(row=1,column=2,padx=60,pady=60)



        def addmarks_page(self):

            self.student_no.set('')
            self.exam_type.set("")


            self.title1.destroy()
            self.frame1.destroy()
            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()
            #*********** ADD STUDENT MARKS PAGE *************
            self.title2=Label(self.root,text='ADD STUDENT MARKS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentmarks,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.backbutton.place(x=20,y=59)

            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exit,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)


            self.stdno=Label(self.frame2,text='Student No.* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdno.grid(row=0,column=0,padx=50,pady=40,sticky='w')
            
            self.stdno_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.student_no)
            self.stdno_entry.grid(row=0,column=1,pady=5)
            

            self.examtype=Label(self.frame2,text='Exam Type:',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.examtype.grid(row=1,column=0,padx=50,pady=10,sticky='w')

            typelist=['ST1','ST2','PUT']
            typemenu=OptionMenu(self.frame2,self.exam_type,*typelist)
            self.exam_type.set("Select Exam Type")
            typemenu.config(width=15,bg='white',fg='black',font=("Garamond",13,'bold'))
            typemenu.grid(row=1,column=1,pady=5)


            self.addmarks=Button(self.frame2,text='Add Marks',font=('arial',13,' bold'),bd=3,bg='lightblue',fg='black',padx=2,pady=2,command=lambda:self.addmarkfunction(self.exam_type.get(),self.year.get()))
            self.addmarks.place(x=170,y=280)

        def addmarkfunction(self,et,y):
            
            b=''
            flag=0


            if self.student_no.get()=='':
                messagebox.showinfo('Warning!','Enter Student No.')
                self.stdno_entry.focus()
            else:
                if et=='ST1':
                    self.mm=25
                    flag=1
                elif et=='ST2':
                    self.mm=50
                    flag=1
                elif et=='PUT':
                    self.mm=100
                    flag=1
                else:
                    self.mm=200
                    messagebox.showinfo('Warning!','Select Exam Type')
                    
            
            if flag==1:    

                
                mc.execute('SELECT count(*) from st1 where stdno=%s and year=%s and exam_type=%s',(self.student_no.get(),self.year.get(),self.exam_type.get(),))
                for i in mc:
                    pass
                
                if i[0]<1:
                
                    mc.execute('SELECT branch from student where student_no=%s and year=%s',(self.student_no.get(),self.year.get(),))

                    for br in mc:
                        b=br[0]
                    self.branchadd.set(b)
                    

                    self.mark1.set('')
                    self.mark2.set('')
                    self.mark3.set('')
                    self.mark4.set('')
                    self.mark5.set('')
                    self.mark6.set('')
                    

                    self.frame3=Frame(self.frame2,bg='lightblue',bd=5,relief=GROOVE)
                    self.frame3.place(x=530,y=0,width=650,height=560)


                    #****************SUBJECTS FOR I YEAR ************************

                    if y=='I':
                        self.stdno_entry.config(state=DISABLED)

                        self.savebutton=Button(self.frame3,text='Save',font=('times new roman',14,'bold'),command=self.savemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                                            
                        if b=='CSE':

                            
                            
                            
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KIT-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-014',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-018',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-012',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-013',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-017',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-016',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-013',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-014',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()

                    
                    #****************SUBJECTS FOR II YEAR ************************

                    if y=='II':
                        self.stdno_entry.config(state=DISABLED)
                        self.savebutton=Button(self.frame3,text='Save',font=('times new roman',14,'bold'),command=self.savemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-034',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-038',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-033',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-036',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()

                            

                    #****************SUBJECTS FOR III YEAR ************************

                    if y=='III':
                        self.stdno_entry.config(state=DISABLED)

                        self.savebutton=Button(self.frame3,text='Save',font=('times new roman',14,'bold'),command=self.savemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KIT-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-054',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-058',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-057',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()


                    #****************SUBJECTS FOR IV YEAR ************************

                    if y=='IV':
                        self.stdno_entry.config(state=DISABLED)

                        self.savebutton=Button(self.frame3,text='Save',font=('times new roman',14,'bold'),command=self.savemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                                            
                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-074',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-078',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')

                            
                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')
                            
                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')
                            
                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':



                            
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()
                        
                else:
                    messagebox.showinfo('Warning!','Marks Already Alloted')
                






        def modifymarks_page(self):

            self.student_no.set('')
            self.exam_type.set("")


            self.title1.destroy()
            self.frame1.destroy()
            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()
            #*********** UPDATE STUDENT MARKS PAGE *************
            self.title2=Label(self.root,text='UPDATE STUDENT MARKS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentmarks,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.backbutton.place(x=20,y=59)

            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exit,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)


            self.stdno=Label(self.frame2,text='Student No.* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdno.grid(row=0,column=0,padx=50,pady=40,sticky='w')
            
            self.stdno_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.student_no)
            self.stdno_entry.grid(row=0,column=1,pady=5)
            

            self.examtype=Label(self.frame2,text='Exam Type:',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.examtype.grid(row=1,column=0,padx=50,pady=10,sticky='w')

            typelist=['ST1','ST2','PUT']
            typemenu=OptionMenu(self.frame2,self.exam_type,*typelist)
            self.exam_type.set("Select Exam Type")
            typemenu.config(width=15,bg='white',fg='black',font=("Garamond",13,'bold'))
            typemenu.grid(row=1,column=1,pady=5)


            self.modifymarks=Button(self.frame2,text='Add Marks',font=('arial',13,' bold'),bd=3,bg='lightblue',fg='black',padx=2,pady=2,command=lambda:self.modifymarkfunction(self.exam_type.get(),self.year.get()))
            self.modifymarks.place(x=170,y=280)

        def modifymarkfunction(self,et,y):

            b=''
            flag=0

            if self.student_no.get()=='':
                messagebox.showinfo('Warning!','Enter Student No.')
                self.stdno_entry.focus()
            else:
                if et=='ST1':
                    self.mm=25
                    flag=1
                elif et=='ST2':
                    self.mm=50
                    flag=1
                elif et=='PUT':
                    self.mm=100
                    flag=1
                else:
                    self.mm=200
                    messagebox.showinfo('Warning!','Select Exam Type')


            
            if flag==1:
                
            
                mc.execute('SELECT count(*) from st1 where stdno=%s and year=%s and exam_type=%s',(self.student_no.get(),self.year.get(),self.exam_type.get(),))
                for i in mc:
                    pass
                            
                if i[0]>0:

                
                    mc.execute('SELECT branch from student where student_no=%s and year=%s',(self.student_no.get(),self.year.get(),))

                    for br in mc:
                        b=br[0]
                    self.branchadd.set(b)
                    

                    self.mark1.set('')
                    self.mark2.set('')
                    self.mark3.set('')
                    self.mark4.set('')
                    self.mark5.set('')
                    self.mark6.set('')
                    

                    self.frame3=Frame(self.frame2,bg='lightblue',bd=5,relief=GROOVE)
                    self.frame3.place(x=530,y=0,width=650,height=560)


                    mc.execute('SELECT sub1,sub2,sub3,sub4,sub5,sub6 from st1 where stdno=%s and year=%s and exam_type=%s',(self.student_no.get(),self.year.get(),self.exam_type.get(),))
                    for mks in mc:
                        self.mark1.set(mks[0])
                        self.mark2.set(mks[1])
                        self.mark3.set(mks[2])
                        self.mark4.set(mks[3])
                        self.mark5.set(mks[4])
                        self.mark6.set(mks[5])


                    #****************SUBJECTS FOR I YEAR ************************

                    if y=='I':
                        self.stdno_entry.config(state=DISABLED)

                        self.updatebutton=Button(self.frame3,text='Update',font=('times new roman',14,'bold'),command=self.updatemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.updatebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)
                          
                        if b=='CSE':  
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')
                                

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KIT-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-014',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-018',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-012',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-013',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-017',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-016',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-013',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-014',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-101',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-102',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-103',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-011',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-015',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()

                    
                    #****************SUBJECTS FOR II YEAR ************************

                    if y=='II':
                        self.stdno_entry.config(state=DISABLED)
                        self.savebutton=Button(self.frame3,text='Uave',font=('times new roman',14,'bold'),command=self.updatemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-034',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-038',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-033',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-036',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-301',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-302',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-303',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-031',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-035',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()

                            

                    #****************SUBJECTS FOR III YEAR ************************

                    if y=='III':
                        self.stdno_entry.config(state=DISABLED)

                        self.savebutton=Button(self.frame3,text='Update',font=('times new roman',14,'bold'),command=self.updatemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KIT-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-054',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-058',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-057',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-501',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-502',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-503',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-051',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-055',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')




                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()


                    #****************SUBJECTS FOR IV YEAR ************************

                    if y=='IV':
                        self.stdno_entry.config(state=DISABLED)

                        self.savebutton=Button(self.frame3,text='Update',font=('times new roman',14,'bold'),command=self.updatemarks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.savebutton.place(x=480,y=200)

                        self.clearbutton=Button(self.frame3,text='Clear',font=('times new roman',14,'bold'),command=self.clear_marks,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
                        self.clearbutton.place(x=480,y=300)


                                            
                        if b=='CSE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCS-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCS-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCS-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCS-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='IT':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCS-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KIT-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KIT-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KIT-074',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KIT-078',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='ME':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KME-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KME-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KME-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KME-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KME-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='EC':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEC-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEC-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEC-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEC-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEC-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')

                            
                        elif b=='EN':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEN-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEN-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEN-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEN-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEN-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')
                            
                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                        elif b=='CE':
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KCE-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KCE-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KCE-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KCE-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KCE-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            self.Entry_marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.Entry_marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')
                            
                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')



                        elif b=='EI':

                            
                            subject=Label(self.frame3,text='Subjects',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            subject.grid(row=0,column=0,padx=50,pady=40,sticky='w')

                            sub1=Label(self.frame3,text='KEI-701',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub1.grid(row=1,column=0,padx=50,pady=10,sticky='w')

                            sub2=Label(self.frame3,text='KEI-702',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub2.grid(row=2,column=0,padx=50,pady=30,sticky='w')

                            sub3=Label(self.frame3,text='KEI-703',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub3.grid(row=3,column=0,padx=50,pady=10,sticky='w')

                            sub4=Label(self.frame3,text='KEI-071',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub4.grid(row=4,column=0,padx=50,pady=30,sticky='w')

                            sub5=Label(self.frame3,text='KEI-075',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub5.grid(row=5,column=0,padx=50,pady=10,sticky='w')

                            sub6=Label(self.frame3,text='KNC',font=('arial',13,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            sub6.grid(row=6,column=0,padx=50,pady=30,sticky='w')



                            marks=Label(self.frame3,text='Marks',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            marks.grid(row=0,column=1,padx=120,pady=40,sticky='w')

                            self.Entry_mark1=Entry(self.frame3,textvariable=self.mark1,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark1.grid(row=1,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark2=Entry(self.frame3,textvariable=self.mark2,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark2.grid(row=2,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark3=Entry(self.frame3,textvariable=self.mark3,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark3.grid(row=3,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark4=Entry(self.frame3,textvariable=self.mark4,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark4.grid(row=4,column=1,padx=120,pady=30,sticky='w')

                            self.Entry_mark5=Entry(self.frame3,textvariable=self.mark5,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark5.grid(row=5,column=1,padx=120,pady=10,sticky='w')

                            self.Entry_mark6=Entry(self.frame3,textvariable=self.mark6,font=('arial',14,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=4)
                            self.Entry_mark6.grid(row=6,column=1,padx=120,pady=30,sticky='w')

                            Label(self.frame3,text='Branch',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=20,pady=40,sticky='w')
                            Label(self.frame3,text=b,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=20,pady=10,sticky='w')


                

                        else:
                            messagebox.showinfo('Warning!','Student Does Not exist...')
                            self.stdno_entry.config(state="normal")
                            self.savebutton.destroy()
                            self.clearbutton.destroy()

                else:
                    try:
                        self.frame3.destroy()
                        messagebox.showinfo("Warning!","Record Not Found!")
                        self.student_no.set('')
                        self.stdno_entry.focus()
                        self.exam_type.set('Select Exam Type')
                    except:
                        messagebox.showinfo("Warning!","Record Not Found!")
                        self.stdno_entry.focus()
                        self.student_no.set('')
                        self.exam_type.set('Select Exam Type')

                        
                    
                







        def addstudent_page(self):
            self.title1.destroy()
            self.frame1.destroy()
            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()
            self.clear()
            #*********** ADD STUDENT PAGE *************
            self.title2=Label(self.root,text='ADD STUDENT DETAILS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.backbutton.place(x=20,y=59)

            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exit,activebackground='lightblue',activeforeground='blue',bd=1,relief=RAISED,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)


            self.stdfname=Label(self.frame2,text='First Name* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdfname.grid(row=0,column=0,padx=50,pady=40,sticky='w')
            
            self.stdfname_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.first_name)
            self.stdfname_entry.grid(row=0,column=1,pady=5)

            self.stdfname_entry.focus()

            self.stdmname=Label(self.frame2,text='Middle Name :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdmname.grid(row=0,column=2,padx=50,pady=5,sticky='w')
            
            self.stdmname_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.middle_name)
            self.stdmname_entry.grid(row=0,column=3,pady=5)


            self.stdlname=Label(self.frame2,text='Last Name* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdlname.grid(row=0,column=4,padx=50,pady=5,sticky='w')
            
            self.stdlname_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.last_name)
            self.stdlname_entry.grid(row=0,column=5,pady=5)
            

            self.stddob=Label(self.frame2,text='D.O.B* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stddob.grid(row=1,column=0,padx=50,pady=30,sticky='w')
            
            self.stddob_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.dob)
            self.stddob_entry.grid(row=1,column=1,pady=20)

            self.stdmob=Label(self.frame2,text='Mobile No* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdmob.grid(row=1,column=2,padx=50,pady=10,sticky='w')
            
            self.stdmob_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.mob_no)
            self.stdmob_entry.grid(row=1,column=3,pady=10)


            self.stdemail=Label(self.frame2,text='Email :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdemail.grid(row=1,column=4,padx=50,pady=10,sticky='w')
            
            self.stdemail_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.email)
            self.stdemail_entry.grid(row=1,column=5,pady=10)


            self.stdfather=Label(self.frame2,text='Father Name* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdfather.grid(row=2,column=0,padx=50,pady=35,sticky='w')
            
            self.stdfather_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.father_name)
            self.stdfather_entry.grid(row=2,column=1,pady=5)
            

            self.stdmother=Label(self.frame2,text='Mother Name* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdmother.grid(row=2,column=2,padx=50,pady=5,sticky='w')
            
            self.stdmother_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.mother_name)
            self.stdmother_entry.grid(row=2,column=3,pady=5)



            self.stdgender=Label(self.frame2,text='Gender* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdgender.grid(row=2,column=4,padx=50,pady=5,sticky='w')
            
            self.stdgender_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.gender)
            self.stdgender_entry.grid(row=2,column=5,pady=5)



            self.stdcourse=Label(self.frame2,text='Course* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdcourse.grid(row=3,column=0,padx=50,pady=5,sticky='w')
            
            self.stdcourse_entry=Label(self.frame2,bg='lightblue',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),text='BTECH',width=16,anchor='w')
            self.stdcourse_entry.grid(row=3,column=1)



            self.stdbranch=Label(self.frame2,text='Branch* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdbranch.grid(row=3,column=2,padx=50,pady=5,sticky='w')

            list29=['CSE','IT','ME','EC','EN','CE','EI']
            droplist29=OptionMenu(self.frame2,self.branch,*list29)
            self.branch.set("Select Branch")
            droplist29.config(width=15,bg='white',fg='black',font=("Garamond",13,'bold'))
            droplist29.grid(row=3,column=3,pady=5)
            

            self.stdno=Label(self.frame2,text='Student No.* :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdno.grid(row=3,column=4,padx=50,pady=40,sticky='w')
            
            self.stdno_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.student_no)
            self.stdno_entry.grid(row=3,column=5,pady=5)



            self.stdblood=Label(self.frame2,text='Blood Group :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdblood.grid(row=4,column=0,padx=50,pady=40,sticky='w')
            
            self.stdblood_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.blood_group)
            self.stdblood_entry.grid(row=4,column=1)

            self.stdyear=Label(self.frame2,text='Year :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdyear.grid(row=4,column=2,padx=50,pady=40,sticky='w')

            self.stdyear_entry=Label(self.frame2,bg='lightblue',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),text=self.year.get(),width=16,anchor='w')
            self.stdyear_entry.grid(row=4,column=3)



            self.stdaddress=Label(self.frame2,text='Address :',font=('arial',14,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
            self.stdaddress.grid(row=4,column=4,padx=50,pady=35,sticky='w')
            
            self.stdaddress_entry=Entry(self.frame2,bg='white',fg='black',bd=2,relief=SUNKEN,font=('Garamond',13,'bold'),textvariable=self.address)
            self.stdaddress_entry.grid(row=4,column=5,pady=5)

            savebutton=Button(self.frame2,text='Save',font=('times new roman',14,'bold'),command=self.save,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
            savebutton.place(x=520,y=490)

            clearbutton=Button(self.frame2,text='Clear',font=('times new roman',14,'bold'),command=self.clear,bd=4,relief=RAISED,bg='lightblue',fg='black',pady=5,padx=20,activebackground='blue',activeforeground='white')
            clearbutton.place(x=670,y=490)        

        def searchmarks_page(self):

            if self.actor=='stu':
                
                self.name1.set('')
                self.marksbranch.set('')
                
                #*********** SEARCH STUDENT MARKS PAGE *************
                self.title2=Label(self.root,text='STUDENT MARKS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.exitbutton.place(x=1247,y=59)
                
                self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)



                stno=Label(self.frame2,text='Student No :',font=('arial',15),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=0,padx=100,pady=30,sticky='w')

                self.stno_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=10,state=DISABLED)
                self.stno_entry.place(x=225,y=28)
                
                
                
                name=Label(self.frame2,text='Student Name :',font=('arial',15),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=500,y=30)

                name_display=Label(self.frame2,textvariable=self.name1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=660,y=30)
                 

                branch=Label(self.frame2,text='Branch :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=900,y=30)

                branch_display=Label(self.frame2,textvariable=self.marksbranch,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=1000,y=30)

                self.framemarks=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.framemarks.place(x=250,y=190,width=830,height=450)
                self.search_marks()


            else:
                self.title1.destroy()
                self.frame1.destroy()
                self.title2.destroy()
                self.frame11.destroy()
                self.backbutton1.destroy()
                self.exitbutton1.destroy()


                self.student1_no.set('')
                self.name1.set('')
                self.marksbranch.set('')
                

                #*********** SEARCH STUDENT MARKS PAGE *************
                self.title2=Label(self.root,text='SEARCH STUDENT MARKS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentmarks,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.exitbutton.place(x=1247,y=59)
                
                self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)

                stno=Label(self.frame2,text='Student No :',font=('arial',15),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=0,padx=100,pady=30,sticky='w')

                self.stno_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=10)
                self.stno_entry.place(x=225,y=28)
                self.stno_entry.focus()
                
                
                name=Label(self.frame2,text='Student Name :',font=('arial',15),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=500,y=30)

                name_display=Label(self.frame2,textvariable=self.name1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=660,y=30)
                 

                branch=Label(self.frame2,text='Branch :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=900,y=30)

                branch_display=Label(self.frame2,textvariable=self.marksbranch,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').place(x=1000,y=30)

                self.framemarks=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.framemarks.place(x=250,y=190,width=830,height=450)



                self.findstd=Button(self.frame2,text='Find',bg='red',font=('times new roman',11,'bold'),command=self.search_marks,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10,pady=3)
                self.findstd.place(x=350,y=28)






        def searchstudent_page(self):
            if self.actor=='stu':

                self.title1.destroy()
                self.frame1.destroy()


                #self.student1_no.set('')
                self.name1.set('')
                self.father1_name.set('')
                self.mother1_name.set('')
                self.course1.set('')
                self.branch1.set('')
                self.dob1.set('')
                self.mob1_no.set('')
                self.gender1.set('')
                self.email1.set('')
                self.blood1_group.set('')
                self.address1.set('                   ')

                #*********** SEARCH STUDENT PAGE *************
                self.title2=Label(self.root,text='STUDENT DETAILS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.exitbutton.place(x=1247,y=59)
                
                self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)

                frame21=Label(self.frame2,bg='green',bd=1,relief=SOLID).place(x=990,y=70,width=200,height=200)
                frame22=Label(self.frame2,bg='green',bd=1,relief=SOLID).place(x=990,y=280,width=200,height=80)


                stno=Label(self.frame2,text='Student No :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=0,padx=50,pady=40,sticky='w')

                stno_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=10,state=DISABLED)
                stno_entry.place(x=235,y=40)
                stno_entry.focus()
                
                
                name=Label(self.frame2,text='Student Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=65,pady=40,sticky='w')

                name_display=Label(self.frame2,textvariable=self.name1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=3,pady=40,sticky='w')
         

                course=Label(self.frame2,text='Course :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=0,padx=50,pady=20,sticky='w')

                course_display=Label(self.frame2,textvariable=self.course1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=1,padx=15,pady=20,sticky='w')
                

                branch=Label(self.frame2,text='Branch :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=65,pady=20,sticky='w')

                branch_display=Label(self.frame2,textvariable=self.branch1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=3,pady=20,sticky='w')


                DOB=Label(self.frame2,text='Date Of Birth :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=0,padx=50,pady=40,sticky='w')

                DOB_display=Label(self.frame2,textvariable=self.dob1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=1,padx=15,pady=40,sticky='w')
                

                MOB=Label(self.frame2,text='Mobile No. :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=2,padx=65,pady=20,sticky='w')

                MOB_display=Label(self.frame2,textvariable=self.mob1_no,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=3,pady=20,sticky='w')


                gen=Label(self.frame2,text='Gender:',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=0,padx=50,pady=20,sticky='w')

                gen_display=Label(self.frame2,textvariable=self.gender1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=1,padx=15,pady=20,sticky='w')
                

                email=Label(self.frame2,text='Email :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=2,padx=65,pady=20,sticky='w')

                email_display=Label(self.frame2,textvariable=self.email1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=3,pady=20,sticky='w')


                father=Label(self.frame2,text='Father Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=0,padx=50,pady=40,sticky='w')

                father_display=Label(self.frame2,textvariable=self.father1_name,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=1,padx=15,pady=40,sticky='w')
                
                mother=Label(self.frame2,text='Mother Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=2,padx=65,pady=40,sticky='w')

                mother_display=Label(self.frame2,textvariable=self.mother1_name,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=3,pady=40,sticky='w')


                address=Label(self.frame2,text='Address :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=0,padx=50,pady=20,sticky='w')

                address_display=Label(self.frame2,textvariable=self.address1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=1,padx=15,pady=20,sticky='w')

                blood=Label(self.frame2,text='Blood Group :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=2,padx=65,pady=20,sticky='w')

                blood_display=Label(self.frame2,textvariable=self.blood1_group,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=3,pady=20,sticky='w')

                self.find_search()
                
            else:
                self.title1.destroy()
                self.frame1.destroy()
                self.title2.destroy()
                self.frame11.destroy()
                self.backbutton1.destroy()
                self.exitbutton1.destroy()


                self.student1_no.set('')
                self.name1.set('')
                self.father1_name.set('')
                self.mother1_name.set('')
                self.course1.set('')
                self.branch1.set('')
                self.dob1.set('')
                self.mob1_no.set('')
                self.gender1.set('')
                self.email1.set('')
                self.blood1_group.set('')
                self.address1.set('                   ')
                

                #*********** SEARCH STUDENT PAGE *************
                self.title2=Label(self.root,text='SEARCH STUDENT',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
                self.title2.pack(fill=X,pady=3)

                self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.backbutton.place(x=20,y=59)
                
                self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
                self.exitbutton.place(x=1247,y=59)
                
                self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
                self.frame2.place(x=20,y=90,width=1285,height=570)

                frame21=Label(self.frame2,bg='green',bd=1,relief=SOLID).place(x=990,y=70,width=200,height=200)
                frame22=Label(self.frame2,bg='green',bd=1,relief=SOLID).place(x=990,y=280,width=200,height=80)



                stno=Label(self.frame2,text='Student No :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=0,padx=50,pady=40,sticky='w')

                stno_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=10)
                stno_entry.place(x=235,y=40)
                stno_entry.focus()
                
                
                name=Label(self.frame2,text='Student Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=65,pady=40,sticky='w')

                name_display=Label(self.frame2,textvariable=self.name1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=3,pady=40,sticky='w')
         

                course=Label(self.frame2,text='Course :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=0,padx=50,pady=20,sticky='w')

                course_display=Label(self.frame2,textvariable=self.course1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=1,padx=15,pady=20,sticky='w')
                

                branch=Label(self.frame2,text='Branch :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=65,pady=20,sticky='w')

                branch_display=Label(self.frame2,textvariable=self.branch1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=3,pady=20,sticky='w')


                DOB=Label(self.frame2,text='Date Of Birth :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=0,padx=50,pady=40,sticky='w')

                DOB_display=Label(self.frame2,textvariable=self.dob1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=1,padx=15,pady=40,sticky='w')
                

                MOB=Label(self.frame2,text='Mobile No. :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=2,padx=65,pady=20,sticky='w')

                MOB_display=Label(self.frame2,textvariable=self.mob1_no,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=3,pady=20,sticky='w')


                gen=Label(self.frame2,text='Gender:',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=0,padx=50,pady=20,sticky='w')

                gen_display=Label(self.frame2,textvariable=self.gender1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=1,padx=15,pady=20,sticky='w')
                

                email=Label(self.frame2,text='Email :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=2,padx=65,pady=20,sticky='w')

                email_display=Label(self.frame2,textvariable=self.email1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=3,pady=20,sticky='w')


                father=Label(self.frame2,text='Father Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=0,padx=50,pady=40,sticky='w')

                father_display=Label(self.frame2,textvariable=self.father1_name,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=1,padx=15,pady=40,sticky='w')
                
                mother=Label(self.frame2,text='Mother Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=2,padx=65,pady=40,sticky='w')

                mother_display=Label(self.frame2,textvariable=self.mother1_name,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=3,pady=40,sticky='w')


                address=Label(self.frame2,text='Address :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=0,padx=50,pady=20,sticky='w')

                address_display=Label(self.frame2,textvariable=self.address1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=1,padx=15,pady=20,sticky='w')

                blood=Label(self.frame2,text='Blood Group :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=2,padx=65,pady=20,sticky='w')

                blood_display=Label(self.frame2,textvariable=self.blood1_group,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=3,pady=20,sticky='w')

                self.findstd=Button(self.frame2,text='Find',bg='red',font=('times new roman',11,'bold'),command=self.find_search,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10,pady=3)
                self.findstd.place(x=360,y=40)




        def updatestudent_page(self):
            self.title1.destroy()
            self.frame1.destroy()

            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()

            self.student1_no.set('')
            self.first_name.set('')
            self.middle_name.set('')
            self.last_name.set('')
            self.father1_name.set('')
            self.mother1_name.set('')
            self.course1.set('')
            self.branch1.set('')
            self.dob1.set('')
            self.mob1_no.set('')
            self.gender1.set('')
            self.email1.set('')
            self.blood1_group.set('')
            self.address1.set('')


            #*********** MODIFY STUDENT PAGE *************
            self.title2=Label(self.root,text='MODIFY STUDENT DETAILS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.backbutton.place(x=20,y=59)

            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)

            stno=Label(self.frame2,text='Student No :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=0,padx=50,pady=40,sticky='w')

            self.stno_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black',width=10)
            self.stno_entry.place(x=235,y=40)
            self.stno_entry.focus()
            
            
            name=Label(self.frame2,text='Student Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=65,pady=40,sticky='w')
            
            self.name11=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=9)
            self.name11.grid(row=0,column=3,pady=40,sticky='w')
            self.name22=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=9)
            self.name22.place(x=850,y=40,height=30)
            self.name33=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=9)
            self.name33.place(x=965,y=40,height=30)

     

            course=Label(self.frame2,text='Course :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=0,padx=50,pady=20,sticky='w')

            self.course11=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.course11.grid(row=1,column=1,padx=15,pady=20,sticky='w')        


            branch=Label(self.frame2,text='Branch :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=1,column=2,padx=65,pady=20,sticky='w')

            self.branch11=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.branch11.grid(row=1,column=3,pady=20,sticky='w')


            DOB=Label(self.frame2,text='Date Of Birth :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=0,padx=50,pady=40,sticky='w')

            self.DOB=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.DOB.grid(row=2,column=1,padx=15,pady=40,sticky='w')
            

            MOB=Label(self.frame2,text='Mobile No. :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=2,column=2,padx=65,pady=20,sticky='w')

            self.MOB=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.MOB.grid(row=2,column=3,pady=20,sticky='w')


            gen=Label(self.frame2,text='Gender:',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=0,padx=50,pady=20,sticky='w')

            self.gen=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.gen.grid(row=3,column=1,padx=15,pady=20,sticky='w')
            

            email=Label(self.frame2,text='Email :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=3,column=2,padx=65,pady=20,sticky='w')

            self.email11=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.email11.grid(row=3,column=3,pady=20,sticky='w')


            father=Label(self.frame2,text='Father Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=0,padx=50,pady=40,sticky='w')

            self.father=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.father.grid(row=4,column=1,padx=15,pady=40,sticky='w')
            
            
            mother=Label(self.frame2,text='Mother Name :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=4,column=2,padx=65,pady=40,sticky='w')

            self.mother=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.mother.grid(row=4,column=3,pady=40,sticky='w')


            address=Label(self.frame2,text='Address :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=0,padx=50,pady=20,sticky='w')

            self.address=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.address.grid(row=5,column=1,padx=15,pady=20,sticky='w')


            blood=Label(self.frame2,text='Blood Group :',font=('arial',14),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=5,column=2,padx=65,pady=20,sticky='w')

            self.blood=Label(self.frame2,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=18)
            self.blood.grid(row=5,column=3,pady=20,sticky='w')

            self.findstd=Button(self.frame2,text='Find',bg='red',font=('times new roman',11,'bold'),command=self.find_modify,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10,pady=3)
            self.findstd.place(x=360,y=40)

            Button(self.frame2,text='Refresh',font=('times new roman',11,'bold'),bg='red',fg='black',activebackground='lightblue',activeforeground='blue',command=self.refresh,bd=0,relief=SOLID,padx=10,pady=3).place(x=420,y=40)
            
            Button(self.frame2,text='Save',font=('times new roman',15,'bold'),command=self.update,bd=5,relief=RAISED,padx=15,pady=8,bg='red',fg='black').place(x=1130,y=460)




        def update(self):
            flag=0
            d=self.dob1.get()
            try:
                date=datetime.date(int(d[:4]),int(d[6]),int(d[8:10]))
                flag=1
            except:
                flag=0
            if self.student1_no.get()=='':
                messagebox.showerror('Alert!','Entry is empty!')

                
            elif self.first_name.get()=='':
                messagebox.showerror('Warning!','Enter First Name')
                self.name11_entry.focus()
                
            elif self.last_name.get()=='':
                messagebox.showerror('Warning!','Enter Last Name')
                self.name33_entry.focus()

            elif self.dob1.get()=='':
                messagebox.showerror('Warning!','Enter D.O.B')
                self.DOB_entry.focus()

            elif self.mob1_no.get()=='':
                messagebox.showerror('Warning!','Enter Mobile Number')
                self.MOB_entry.focus()

            elif self.father1_name.get()=='':
                messagebox.showerror('Warning!','Enter Father Name')
                self.father_entry.focus()

            elif self.mother1_name.get()=='':
                messagebox.showerror('Warning!','Enter Mother Name')
                self.mother_entry.focus()

            elif self.gender1.get()=='':
                messagebox.showerror('Warning!','Enter Gender')
                self.gen_entry.focus()


            elif self.branch1.get()=='':
                messagebox.showerror('Warning!','Enter Branch')
                self.branch11_entry.focus()

            
            elif flag==0:
                messagebox.showinfo('Alert!','Enter Date in YYYY-MM-DD format')
                self.DOB_entry.focus()
                
                
            elif self.mob1_no.get().isnumeric()==False or len(self.mob1_no.get())<10:
                messagebox.showinfo('Alert!','Enter 10 Digits Mobile Number')
                self.MOB_entry.focus()
                    
            

            else:
                yesno=messagebox.askyesno('Alert!','Do you really want to modify it.')
                if yesno>0:
                    modifyformula=('UPDATE student SET First_Name=%s,Middle_Name=%s,Last_Name=%s,Father_Name=%s,Mother_Name=%s,branch=%s,dob=%s,mob=%s,gender=%s,email=%s,blood_group=%s,address=%s WHERE student_no=%s')
                    update_student_info=(self.first_name.get(),self.middle_name.get(),self.last_name.get(),self.father1_name.get(),self.mother1_name.get(),self.branch1.get(),self.dob1.get(),self.mob1_no.get(),self.gender1.get(),self.email1.get(),self.blood1_group.get(),self.address1.get(),eval(self.student1_no.get()))
                    mc.execute(modifyformula,update_student_info)
                    mydb.commit()
                    messagebox.showinfo('Greets!','Data successfully updated')
                    self.stno.destroy()
                    self.name11_entry.destroy()
                    self.name22_entry.destroy()
                    self.name33_entry.destroy()
                    self.course11_entry.destroy()
                    self.branch11_entry.destroy()
                    self.DOB_entry.destroy()
                    self.MOB_entry.destroy()
                    self.gen_entry.destroy()
                    self.email11_entry.destroy()
                    self.father_entry.destroy()
                    self.mother_entry.destroy()
                    self.address_entry.destroy()
                    self.blood_entry.destroy()

                    self.title2.destroy()
                    self.frame2.destroy()
                    self.backbutton.destroy()
                    self.exitbutton.destroy()
                    self.updatestudent_page()

                

        def refresh(self):
                self.title2.destroy()
                self.frame2.destroy()
                self.backbutton.destroy()
                self.exitbutton.destroy()
                self.updatestudent_page()

            


        def displaystudent_page(self):
            self.title1.destroy()
            self.frame1.destroy()

            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()

            #*********** DISPLAY STUDENT PAGE *************
            self.title2=Label(self.root,text='DISPLAY STUDENTS DETAILS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.backbutton.place(x=20,y=59)

            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)


            
            
            self.horizontal_scrollbar=Scrollbar(self.frame2,orient=HORIZONTAL,activebackground='red',bg='lightblue')
            self.horizontal_scrollbar.pack(fill=X,side=BOTTOM)

            self.vertical_scrollbar=Scrollbar(self.frame2,orient=VERTICAL,activebackground='red')
            self.vertical_scrollbar.pack(fill=Y,side=RIGHT)
                    


            self.canvas=Canvas(self.frame2,bg='lightblue',bd=0,relief=SUNKEN)
            self.canvas.pack(fill=BOTH,expand=True,pady=31)

            self.horizontal_scrollbar.config(command=self.canvas.xview)
            self.vertical_scrollbar.config(command=self.canvas.yview)



            self.canvas.config(yscrollcommand=self.vertical_scrollbar.set,xscrollcommand=self.horizontal_scrollbar.set)

            self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox(ALL)))

            self.frame21=Frame(self.canvas,bg='lightblue',bd=3,relief=GROOVE)
            self.canvas.create_window((0,0),window=self.frame21,anchor='nw')

            select_branch=Label(self.frame2,text='Display By Branch:',font=('times new roman',11,'bold'),bd=0,relief=SOLID,bg='lightblue',fg='black',pady=7)
            select_branch.place(x=450,y=0)

            list2=['ALL','CSE','IT','ME','EC','EN','CE','EI']
            droplist2=OptionMenu(self.frame2,self.branch,*list2)
            self.branch.set("ALL")
            droplist2.config(width=10,bg='lightblue',fg='black',font=("times new roman",11,'bold'),pady=3,bd=1)
            droplist2.place(x=600,y= 2)

            Button(self.frame2,text='Sort',bg='blue',fg='white',font=('times new roman',11,'bold'),command=self.display_by_branch,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10).place(x=750,y=2)



            Label(self.frame21,text="Student No.",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=0,pady=5)
            Label(self.frame21,text="Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=1,pady=5)
            Label(self.frame21,text="Year",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=2,pady=5)
            Label(self.frame21,text="Course",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=3,pady=5)
            Label(self.frame21,text="Branch",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=4,pady=5)
            Label(self.frame21,text="D.O.B",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=5,pady=5)
            Label(self.frame21,text="Gender",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=6,pady=5)
            Label(self.frame21,text="Mobile No.",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=7,pady=5)
            Label(self.frame21,text="Father Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=8,pady=5)
            Label(self.frame21,text="Mother Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=9,pady=5)
            Label(self.frame21,text="Email",fg="white",bg="blue",relief='groove',width=30,font=("caliber",16,"bold")).grid(row=0,column=10,pady=5)
            Label(self.frame21,text="Blood Group",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=11,pady=5)
            Label(self.frame21,text="Address",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=12,pady=5)

            display_by_branch=('SELECT * FROM student WHERE year=%s')
            mc.execute(display_by_branch,(self.year.get(),))
            
            r=1
            self.totalstudent=0
            for i in mc:
                self.totalstudent+=1
                self.l11=Label(self.frame21,text=i[0],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14,"bold"),bd=1)
                self.l11.grid(row=r,column=0)
                self.l22=Label(self.frame21,text='{} {} {}'.format(i[1],i[2],i[3]),fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",16),bd=1,anchor='w')
                self.l22.grid(row=r,column=1)
                self.l33=Label(self.frame21,text=i[13],fg="black",bg="lightblue",relief='groove',width=12,font=("time new roman",14),bd=1)
                self.l33.grid(row=r,column=2)
                self.l44=Label(self.frame21,text=i[6],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                self.l44.grid(row=r,column=3)
                self.l55=Label(self.frame21,text=i[7],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                self.l55.grid(row=r,column=4)
                self.l66=Label(self.frame21,text=i[8],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                self.l66.grid(row=r,column=5)
                self.l77=Label(self.frame21,text=i[10],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14),bd=1,anchor='w')
                self.l77.grid(row=r,column=6)
                self.l88=Label(self.frame21,text=i[9],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                self.l88.grid(row=r,column=7)
                self.l99=Label(self.frame21,text=i[4],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                self.l99.grid(row=r,column=8)
                self.l1010=Label(self.frame21,text=i[5],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                self.l1010.grid(row=r,column=9)
                self.l1111=Label(self.frame21,text=i[11],fg="black",bg="lightblue",relief='groove',width=30,font=("time new roman",14),bd=1,anchor='w')
                self.l1111.grid(row=r,column=10)
                self.l1212=Label(self.frame21,text=i[12],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                self.l1212.grid(row=r,column=11)
                self.l1313=Label(self.frame21,text=i[14],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                self.l1313.grid(row=r,column=12)
                r+=1
        


        def display_by_branch(self):
            self.frame21.destroy()

            self.frame21=Frame(self.canvas,bg='lightblue',bd=3,relief=GROOVE)
            self.canvas.create_window((0,0),window=self.frame21,anchor='nw')

            Label(self.frame21,text="Student No.",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=0,pady=5)
            Label(self.frame21,text="Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=1,pady=5)
            Label(self.frame21,text="Year",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=2,pady=5)
            Label(self.frame21,text="Course",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=3,pady=5)
            Label(self.frame21,text="Branch",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=4,pady=5)
            Label(self.frame21,text="D.O.B",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=5,pady=5)
            Label(self.frame21,text="Gender",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=6,pady=5)
            Label(self.frame21,text="Mobile No.",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=7,pady=5)
            Label(self.frame21,text="Father Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=8,pady=5)
            Label(self.frame21,text="Mother Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=9,pady=5)
            Label(self.frame21,text="Email",fg="white",bg="blue",relief='groove',width=30,font=("caliber",16,"bold")).grid(row=0,column=10,pady=5)
            Label(self.frame21,text="Blood Group",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=11,pady=5)
            Label(self.frame21,text="Address",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=12,pady=5)



                                    
        
            if self.branch.get()!='ALL':
                form1=('SELECT count(*) FROM student WHERE year=%s and branch=%s')
                mc.execute(form1,(self.year.get(),self.branch.get(),))

                for j in mc:
                    pass
                
                if j[0]!=0:
    
                    form=('SELECT * FROM student WHERE year=%s and branch=%s')
                    mc.execute(form,(self.year.get(),self.branch.get(),))

                    r=1
                    for i in mc:
                        
                        self.l11=Label(self.frame21,text=i[0],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14,"bold"),bd=1)
                        self.l11.grid(row=r,column=0)
                        self.l22=Label(self.frame21,text='{} {} {}'.format(i[1],i[2],i[3]),fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",16),bd=1,anchor='w')
                        self.l22.grid(row=r,column=1)
                        self.l33=Label(self.frame21,text=i[13],fg="black",bg="lightblue",relief='groove',width=12,font=("time new roman",14),bd=1)
                        self.l33.grid(row=r,column=2)
                        self.l44=Label(self.frame21,text=i[6],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                        self.l44.grid(row=r,column=3)
                        self.l55=Label(self.frame21,text=i[7],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                        self.l55.grid(row=r,column=4)
                        self.l66=Label(self.frame21,text=i[8],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                        self.l66.grid(row=r,column=5)
                        self.l77=Label(self.frame21,text=i[10],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14),bd=1,anchor='w')
                        self.l77.grid(row=r,column=6)
                        self.l88=Label(self.frame21,text=i[9],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                        self.l88.grid(row=r,column=7)
                        self.l99=Label(self.frame21,text=i[4],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                        self.l99.grid(row=r,column=8)
                        self.l1010=Label(self.frame21,text=i[5],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                        self.l1010.grid(row=r,column=9)
                        self.l1111=Label(self.frame21,text=i[11],fg="black",bg="lightblue",relief='groove',width=30,font=("time new roman",14),bd=1,anchor='w')
                        self.l1111.grid(row=r,column=10)
                        self.l1212=Label(self.frame21,text=i[12],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                        self.l1212.grid(row=r,column=11) 
                        self.l1313=Label(self.frame21,text=i[14],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                        self.l1313.grid(row=r,column=12)
                        r+=1
                else:
                    messagebox.showinfo('Warning!','No Record Found!')
            else:

                display_by_branch=('SELECT * FROM student WHERE year=%s')
                mc.execute(display_by_branch,(self.year.get(),))
                
                r=1

                for i in mc:
                    self.l11=Label(self.frame21,text=i[0],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14,"bold"),bd=1)
                    self.l11.grid(row=r,column=0)
                    self.l22=Label(self.frame21,text='{} {} {}'.format(i[1],i[2],i[3]),fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",16),bd=1,anchor='w')
                    self.l22.grid(row=r,column=1)
                    self.l33=Label(self.frame21,text=i[13],fg="black",bg="lightblue",relief='groove',width=12,font=("time new roman",14),bd=1)
                    self.l33.grid(row=r,column=2)
                    self.l44=Label(self.frame21,text=i[6],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                    self.l44.grid(row=r,column=3)
                    self.l55=Label(self.frame21,text=i[7],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                    self.l55.grid(row=r,column=4)
                    self.l66=Label(self.frame21,text=i[8],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                    self.l66.grid(row=r,column=5)
                    self.l77=Label(self.frame21,text=i[10],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14),bd=1,anchor='w')
                    self.l77.grid(row=r,column=6)
                    self.l88=Label(self.frame21,text=i[9],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                    self.l88.grid(row=r,column=7)
                    self.l99=Label(self.frame21,text=i[4],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                    self.l99.grid(row=r,column=8)
                    self.l1010=Label(self.frame21,text=i[5],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                    self.l1010.grid(row=r,column=9)
                    self.l1111=Label(self.frame21,text=i[11],fg="black",bg="lightblue",relief='groove',width=30,font=("time new roman",14),bd=1,anchor='w')
                    self.l1111.grid(row=r,column=10)
                    self.l1212=Label(self.frame21,text=i[12],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1,anchor='w')
                    self.l1212.grid(row=r,column=11)
                    
                    self.l1313=Label(self.frame21,text=i[14],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1,anchor='w')
                    self.l1313.grid(row=r,column=12)
                    r+=1
        

                

        def deletestudent_page(self):
            self.title1.destroy()
            self.frame1.destroy()

            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()
            
            self.student1_no.set('')
            #*********** DELETE STUDENT PAGE *************
            self.title2=Label(self.root,text='DELETE STUDENT DETAILS',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.backbutton.place(x=20,y=59)
            
            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)

            Label(self.frame2,text='Student Number :',font=('arial bold',14),bg='lightblue',fg='black',bd=0,relief=SOLID).place(x=430,y=50)
            self.delete_entry=Entry(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=10)
            self.delete_entry.place(x=630,y=50)

            self.delete_entry.focus()

            Button(self.frame2,text='Find',bg='red',font=('times new roman',11,'bold'),command=self.find_delete,activebackground='lightblue',activeforeground='blue',bd=3,relief=RAISED,padx=10).place(x=780,y=47)

            
            horizontal_scrollbar=Scrollbar(self.frame2,orient=HORIZONTAL,activebackground='red',bg='lightblue')
            horizontal_scrollbar.pack(fill=X,side=BOTTOM)

            canvas=Canvas(self.frame2,bg='lightblue',bd=0,relief=SUNKEN,height=400)
            canvas.pack(fill=X,side=BOTTOM)

            horizontal_scrollbar.config(command=canvas.xview)

            canvas.config(xscrollcommand=horizontal_scrollbar.set)

            canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox(ALL)))

            self.frame21=Frame(canvas,bg='lightblue',bd=5,relief=GROOVE)
            canvas.create_window((0,0),window=self.frame21,anchor='nw')

            Label(self.frame21,text="Student No.",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=0,pady=5)
            Label(self.frame21,text="Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=1,pady=5)
            Label(self.frame21,text="Year",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=2,pady=5)
            Label(self.frame21,text="Course",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=3,pady=5)
            Label(self.frame21,text="Branch",fg="white",bg="blue",relief='groove',width=14,font=("caliber",16,"bold")).grid(row=0,column=4,pady=5)
            Label(self.frame21,text="D.O.B",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=5,pady=5)
            Label(self.frame21,text="Gender",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=6,pady=5)
            Label(self.frame21,text="Mobile No.",fg="white",bg="blue",relief='groove',width=15,font=("caliber",16,"bold")).grid(row=0,column=7,pady=5)
            Label(self.frame21,text="Father Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=8,pady=5)
            Label(self.frame21,text="Mother Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=9,pady=5)
            Label(self.frame21,text="Email",fg="white",bg="blue",relief='groove',width=30,font=("caliber",16,"bold")).grid(row=0,column=10,pady=5)
            Label(self.frame21,text="Blood Group",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=11,pady=5)
            Label(self.frame21,text="Address",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=12,pady=5)

            Button(self.frame2,text='DELETE',font=('times new roman',18,'bold'),bd=5,relief=RAISED,padx=10,pady=10,bg='red',fg='black',command=self.delete).place(x=575,y=400)



        def delete(self):
            yn=messagebox.askyesno('Warning','Do you really want to Delete')
            if yn>0:
                if self.student1_no.get()!='':
                    form=('DELETE FROM student WHERE student_no=%s')
                    mc.execute(form,(eval(self.student1_no.get()),))
                    mydb.commit()

                    mc.execute('DELETE FROM st1 WHERE stdno=%s',(self.student1_no.get(),))
                    mydb.commit()
        
                    messagebox.showinfo('Greets','Record Successfully Deleted')
                    self.student1_no.set('')
                    self.l1.destroy()
                    self.l2.destroy()
                    self.l3.destroy()
                    self.l4.destroy()
                    self.l5.destroy()
                    self.l6.destroy()
                    self.l7.destroy()
                    self.l8.destroy()
                    self.l9.destroy()
                    self.l10.destroy()
                    self.l11.destroy()
                    self.l12.destroy()
                    self.l13.destroy()

                else:
                    messagebox.showerror('Alert!','Entry is empty!')

                
            
        def find_delete(self):
            if self.student1_no.get()=='':
                self.delete_entry.focus()
                messagebox.showerror('Alert!','Entry is empty!')
            else:
                form=('SELECT COUNT(*) FROM student WHERE Student_no=%s and year=%s')
                mc.execute(form,(eval(self.student1_no.get()),self.year.get(),))

                for row in mc:
                     pass
                if row[0]>0:
                    delete_formula=('SELECT * FROM student where student_no=%s')
                    mc.execute(delete_formula,(eval(self.student1_no.get()),))
                    
                    r=1

                    for i in mc:
                        self.l1=Label(self.frame21,text=i[0],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14,"bold"),bd=1)
                        self.l1.grid(row=r,column=0)
                        self.l2=Label(self.frame21,text='{} {} {}'.format(i[1],i[2],i[3]),fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",16),bd=1)
                        self.l2.grid(row=r,column=1)
                        self.l3=Label(self.frame21,text=i[13],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",16),bd=1)
                        self.l3.grid(row=r,column=2)
                        self.l4=Label(self.frame21,text=i[6],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1)
                        self.l4.grid(row=r,column=3)
                        self.l5=Label(self.frame21,text=i[7],fg="black",bg="lightblue",relief='groove',width=14,font=("time new roman",14),bd=1)
                        self.l5.grid(row=r,column=4)
                        self.l6=Label(self.frame21,text=i[8],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                        self.l6.grid(row=r,column=5)
                        self.l7=Label(self.frame21,text=i[10],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14),bd=1)
                        self.l7.grid(row=r,column=6)
                        self.l8=Label(self.frame21,text=i[9],fg="black",bg="lightblue",relief='groove',width=15,font=("time new roman",14),bd=1)
                        self.l8.grid(row=r,column=7)
                        self.l9=Label(self.frame21,text=i[4],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1)
                        self.l9.grid(row=r,column=8)
                        self.l10=Label(self.frame21,text=i[5],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1)
                        self.l10.grid(row=r,column=9)
                        self.l11=Label(self.frame21,text=i[11],fg="black",bg="lightblue",relief='groove',width=30,font=("time new roman",14),bd=1)
                        self.l11.grid(row=r,column=10)
                        self.l12=Label(self.frame21,text=i[12],fg="black",bg="lightblue",relief='groove',width=10,font=("time new roman",14),bd=1)
                        self.l12.grid(row=r,column=11)
                        self.l13=Label(self.frame21,text=i[14],fg="black",bg="lightblue",relief='groove',width=20,font=("time new roman",14),bd=1)
                        self.l13.grid(row=r,column=12)
                        r+=1
                else:
                    try:
                        self.l1.destroy()
                        self.l2.destroy()
                        self.l3.destroy()
                        self.l4.destroy()
                        self.l5.destroy()
                        self.l6.destroy()
                        self.l7.destroy()
                        self.l8.destroy()
                        self.l9.destroy()
                        self.l10.destroy()
                        self.l11.destroy()
                        self.l12.destroy()
                        self.l13.destroy()
                        messagebox.showinfo('Alert!','Sorry no record found')
                        self.student1_no.set('')
                        self.delete_entry.focus()

                    except:
                        messagebox.showinfo('Alert!','Sorry no record found')
                        self.student1_no.set('')
                        self.delete_entry.focus()

                    
                    

        def studentattendance_page(self):
            self.title1.destroy()
            self.frame1.destroy()
            
            self.title2.destroy()
            self.frame11.destroy()
            self.backbutton1.destroy()
            self.exitbutton1.destroy()
            #******************ATTENDANCE VARIABLES ***************

            self.length=0

            display_by_branch=('SELECT * FROM student WHERE year=%s')
            mc.execute(display_by_branch,(self.year.get(),))

            for i in mc:
                self.length+=1

            
            self.sdate=StringVar()
            self.tdate=StringVar()

            self.tatt=[0]*self.length
            self.patt=[0]*self.length

            self.perc=[0]*self.length
            

            #***********  STUDENT ATTENDANCE PAGE *************
            self.title2=Label(self.root,text='STUDENT ATTENDANCE',font=('arial',18,'bold'),bd=5,relief=RAISED,bg='blue',fg='white',pady=7)
            self.title2.pack(fill=X,pady=3)

            self.backbutton=Button(self.root,text='Back',bg='red',font=('times new roman',11,'bold'),command=self.back_2_studentdetails,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.backbutton.place(x=20,y=59)
            
            self.exitbutton=Button(self.root,text='Exit',bg='red',font=('times new roman',11,'bold'),command=self.exitmainpage,activebackground='lightblue',activeforeground='blue',bd=0,relief=SOLID,padx=10)
            self.exitbutton.place(x=1247,y=59)
            
            self.frame2=Frame(self.root,bg='lightblue',bd=5,relief=GROOVE)
            self.frame2.place(x=20,y=90,width=1285,height=570)

            vertical_scrollbar=Scrollbar(self.frame2,orient=VERTICAL,activebackground='red',bg='lightblue')
            vertical_scrollbar.pack(fill=Y,side=RIGHT)

            canvas=Canvas(self.frame2,bg='lightblue',bd=0,relief=SUNKEN,width=940)
            canvas.pack(pady=30,fill=Y,expand=True)

            vertical_scrollbar.config(command=canvas.yview)

            canvas.config(yscrollcommand=vertical_scrollbar.set)

            canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox(ALL)))

            self.frame21=Frame(canvas,bg='lightblue',bd=5,relief=GROOVE)

            canvas.create_window((0,0),window=self.frame21,anchor='nw')

            Label(self.frame21,text="Student No.",fg="white",bg="blue",relief='groove',width=10,font=("caliber",16,"bold")).grid(row=0,column=0)
            Label(self.frame21,text="Name",fg="white",bg="blue",relief='groove',width=20,font=("caliber",16,"bold")).grid(row=0,column=1)
            Label(self.frame21,text="Attendance",fg="white",bg="blue",relief='groove',width=40,font=("caliber",16,"bold")).grid(row=0,column=2)
            

            Label(self.frame21,fg="white",bg="lightblue",relief='groove',width=10,height=3,font=("caliber",16,"bold")).grid(row=1,column=0)
            Label(self.frame21,fg="white",bg="lightblue",relief='groove',width=20,height=3,font=("caliber",16,"bold")).grid(row=1,column=1)


            #**********box 1****************
            Label(self.frame21,bg="lightblue",width=74,bd=2,height=2,relief=SOLID).place(x=404,y=32)

            #**********box 2****************
            Label(self.frame21,bg="lightblue",width=74,bd=2,height=2,relief=SOLID).place(x=404,y=65)

            Label(self.frame21,text='TOTAL',font=("caliber",14,"bold"),bg="lightblue",bd=0,relief=SOLID).place(x=458,y=71)

            Label(self.frame21,bg="lightblue",width=0,bd=2,height=2,relief=SOLID).place(x=570,y=65)
            
            Label(self.frame21,text='PRESENT',font=("caliber",14,"bold"),bg="lightblue",bd=0,relief=SOLID).place(x=620,y=71)

            Label(self.frame21,bg="lightblue",width=0,bd=2,height=2,relief=SOLID).place(x=750,y=65)

            Label(self.frame21,text='PERCENT(%)',font=("caliber",14,"bold"),bg="lightblue",bd=0,relief=SOLID).place(x=780,y=71)

            

            Label(self.frame21,text="From Date",fg="black",bg="lightblue",relief='groove',width=10,font=("caliber",13,"bold"),bd=0).place(x=435,y=38)
            Entry(self.frame21,fg="black",bg="white",relief=SUNKEN,width=10,font=("caliber",13,"bold"),bd=2,textvariable=self.sdate).place(x=550,y=37)

            Label(self.frame21,text="To Date",fg="black",bg="lightblue",relief='groove',width=10,font=("caliber",13,"bold"),bd=0).place(x=655,y=38)
            Entry(self.frame21,fg="black",bg="white",relief=SUNKEN,width=10,font=("caliber",13,"bold"),bd=2,textvariable=self.tdate).place(x=760,y=37)

            Button(self.frame2,text='Save',bg='lightblue',fg='black',font=("caliber",12,"bold"),bd=3,command=self.saveattendance).pack(pady=10)

            
            r=2
            r2=0

            display_by_branch=('SELECT * FROM student WHERE year=%s')
            mc.execute(display_by_branch,(self.year.get(),))

            self.m=0

            for i in mc:
                Label(self.frame21,text=i[0],fg="black",bg="lightblue",relief='groove',width=11,font=("time new roman",14,"bold"),bd=1,pady=4).grid(row=r,column=0)
                Label(self.frame21,text='{} {} {}'.format(i[1],i[2],i[3]),fg="black",bg="lightblue",relief='groove',width=24,font=("time new roman",14),bd=1,anchor='w',pady=4).grid(row=r,column=1)
                boxframe=Frame(self.frame21,bg="lightblue",width=525,bd=2,relief=SOLID,height=35)
                boxframe.grid(row=r,column=2,pady=1)
                
                self.tatten=Entry(boxframe,fg="black",bg="white",relief='sunken',width=6,font=("time new roman",14,'bold'),justify='center',bd=2)
                self.tatten.grid(row=0,column=0,padx=44)

                

                Label(boxframe,bg="lightblue",width=0,bd=2,height=1,pady=7,relief=SOLID).grid(row=0,column=1,padx=3)

                self.patten=Entry(boxframe,fg="black",bg="white",relief='sunken',width=6,font=("time new roman",14,'bold'),justify='center',bd=2)
                self.patten.grid(row=0,column=2,padx=47)

                

                Label(boxframe,bg="lightblue",width=0,bd=2,height=1,pady=7,relief=SOLID).grid(row=0,column=3,padx=5)

                self.percatten=Label(boxframe,fg="black",bg="lightblue",relief='sunken',width=6,font=("time new roman",14,'bold'),justify='center',bd=2)
                self.percatten.grid(row=0,column=4,padx=44)
                self.percatten.config(text=self.perc[self.m])
                self.m+=1


                r+=1



        

        def saveattendance(self):

            pass

                    
            
            
            
            


            
        

        def exitmainpage(self):
            yn=messagebox.askyesno('Alert!','Do you want to Exit')
            if yn>0:
                self.root.destroy()



        def savemarks(self):        
            if self.student_no.get()=='':
                messagebox.showerror('Warning!','Enter Student Number')
                self.stdno_entry.focus()

            elif self.mark1.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 1st Subject')
                self.Entry_mark1.focus()

            elif self.mark2.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 2nd Subject')
                self.Entry_mark2.focus()
                
            elif self.mark3.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 3rd Subject')
                self.Entry_mark3.focus()

            elif self.mark4.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 4th Subject')
                self.Entry_mark4.focus()

            elif self.mark5.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 5th Subject')
                self.Entry_mark5.focus()

            elif self.mark6.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 6th Subject')
                self.Entry_mark6.focus()

            elif (self.student_no.get()).isnumeric()==False or len(self.student_no.get())<7:
                messagebox.showinfo('Alert!','Enter 7 Digits Student Number')
                self.student_no.set('')
                self.stdno_entry.focus()

            elif eval(self.mark1.get())<0 or eval(self.mark1.get())>self.mm or (self.mark1.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark1.set('')
                self.Entry_mark1.focus()

            elif eval(self.mark2.get())<0 or eval(self.mark2.get())>self.mm or (self.mark2.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark2.set('')
                self.Entry_mark2.focus()

            elif eval(self.mark3.get())<0 or eval(self.mark3.get())>self.mm or (self.mark3.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark3.set('')
                self.Entry_mark3.focus()

            elif eval(self.mark4.get())<0 or eval(self.mark4.get())>self.mm or (self.mark4.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark4.set('')
                self.Entry_mark4.focus()

            elif eval(self.mark5.get())<0 or eval(self.mark5.get())>self.mm or (self.mark5.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark5.set('')
                self.Entry_mark5.focus()

            elif eval(self.mark6.get())<0 or eval(self.mark6.get())>self.mm or (self.mark6.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark6.set('')
                self.Entry_mark6.focus()


            else:
                stno=eval(self.student_no.get())
                mc.execute('SELECT stdno FROM st1')
                stlist=[]
                for stu_no in mc:
                    stlist.append(stu_no[0])


                if stno in stlist:
                    messagebox.showinfo('Warning!','Student Number already exists')
                    self.student_no.set('')
                    self.stdno_entry.focus()
                else:
                    
                    sqlFormula_marks=('INSERT INTO st1 (stdno,year,exam_type,sub1,sub2,sub3,sub4,sub5,sub6,branch) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                    marks_info=(stno,self.year.get(),self.exam_type.get(),self.mark1.get(),self.mark2.get(),self.mark3.get(),self.mark4.get(),self.mark5.get(),self.mark6.get(),self.branchadd.get())
                    mc.execute(sqlFormula_marks,marks_info)
                    mydb.commit()

                    messagebox.showinfo('Greets!','Data Sucsessfully saved')
                    self.frame3.destroy()
                    self.stdno_entry.config(state="normal")
                    self.student_no.set('')
                    self.stdno_entry.focus()
                    self.exam_type.set('Select Exam Type')
                        


        def updatemarks(self):        
            if self.student_no.get()=='':
                messagebox.showerror('Warning!','Enter Student Number')
                self.stdno_entry.focus()

            elif self.mark1.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 1st Subject')
                self.Entry_mark1.focus()

            elif self.mark2.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 2nd Subject')
                self.Entry_mark2.focus()
                
            elif self.mark3.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 3rd Subject')
                self.Entry_mark3.focus()

            elif self.mark4.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 4th Subject')
                self.Entry_mark4.focus()

            elif self.mark5.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 5th Subject')
                self.Entry_mark5.focus()

            elif self.mark6.get()=='':
                messagebox.showerror('Warning!','Enter Marks of 6th Subject')
                self.Entry_mark6.focus()

            elif (self.student_no.get()).isnumeric()==False or len(self.student_no.get())<7:
                messagebox.showinfo('Alert!','Enter 7 Digits Student Number')
                self.student_no.set('')
                self.stdno_entry.focus()

            elif eval(self.mark1.get())<0 or eval(self.mark1.get())>self.mm or (self.mark1.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark1.set('')
                self.Entry_mark1.focus()

            elif eval(self.mark2.get())<0 or eval(self.mark2.get())>self.mm or (self.mark2.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark2.set('')
                self.Entry_mark2.focus()

            elif eval(self.mark3.get())<0 or eval(self.mark3.get())>self.mm or (self.mark3.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark3.set('')
                self.Entry_mark3.focus()

            elif eval(self.mark4.get())<0 or eval(self.mark4.get())>self.mm or (self.mark4.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark4.set('')
                self.Entry_mark4.focus()

            elif eval(self.mark5.get())<0 or eval(self.mark5.get())>self.mm or (self.mark5.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark5.set('')
                self.Entry_mark5.focus()

            elif eval(self.mark6.get())<0 or eval(self.mark6.get())>self.mm or (self.mark6.get()).isnumeric()==False:
                messagebox.showinfo('Alert!','Enter Only Digit in range 0 and {}'.format(self.mm))
                self.mark6.set('')
                self.Entry_mark6.focus()


            else:
                yesnoupdatemarks=messagebox.askyesno('Alert!','Do you really want to modify it.')
                if yesnoupdatemarks>0:
                    update_marks=('UPDATE st1 SET sub1=%s,sub2=%s,sub3=%s,sub4=%s,sub5=%s,sub6=%s WHERE stdno=%s and exam_type=%s')
                    updatemarks_info=(self.mark1.get(),self.mark2.get(),self.mark3.get(),self.mark4.get(),self.mark5.get(),self.mark6.get(),self.student_no.get(),self.exam_type.get())
                    mc.execute(update_marks,updatemarks_info)
                    mydb.commit()

                    messagebox.showinfo('Greets!','Data Sucsessfully updatted')
                    self.frame3.destroy()
                    self.stdno_entry.config(state="normal")
                    self.student_no.set('')
                    self.stdno_entry.focus()
                    self.exam_type.set('Select Exam Type')


                

        def save(self):
            flag=0
            d=self.dob.get()
            try:
                date=datetime.date(int(d[:4]),int(d[6]),int(d[8:10]))
                flag=1
            except:
                flag=0
                
            if self.first_name.get()=='':
                messagebox.showerror('Warning!','Enter First Name')
                self.stdfname_entry.focus()
            elif self.last_name.get()=='':
                messagebox.showerror('Warning!','Enter Last Name')
                self.stdlname_entry.focus()

            elif self.dob.get()=='':
                messagebox.showerror('Warning!','Enter D.O.B')
                self.stddob_entry.focus()

            elif self.mob_no.get()=='':
                messagebox.showerror('Warning!','Enter Mobile Number')
                self.stdmob_entry.focus()

            elif self.father_name.get()=='':
                messagebox.showerror('Warning!','Enter Father Name')
                self.stdfather_entry.focus()

            elif self.mother_name.get()=='':
                messagebox.showerror('Warning!','Enter Mother Name')
                self.stdmother_entry.focus()

            elif self.gender.get()=='':
                messagebox.showerror('Warning!','Enter Gender')
                self.stdgender_entry.focus()

            elif self.branch.get()=='':
                messagebox.showerror('Warning!','Enter Branch')
                self.stdbranch_entry.focus()

            elif self.student_no.get()=='':
                messagebox.showerror('Warning!','Enter Student Number')
                self.stdno_entry.focus()

            
            elif flag==0:
                messagebox.showinfo('Alert!','Enter Date in YYYY-MM-DD format')
                self.dob.set('')
                self.stddob_entry.focus()
                
                
            elif self.mob_no.get().isnumeric()==False or len(self.mob_no.get())<10:
                messagebox.showinfo('Alert!','Enter 10 Digits Mobile Number')
                self.mob_no.set('')
                self.stdmob_entry.focus()
                    
            elif (self.student_no.get()).isnumeric()==False or len(self.student_no.get())<7:
                messagebox.showinfo('Alert!','Enter 7 Digits Student Number')
                self.student_no.set('')
                self.stdno_entry.focus()


                                   
            else:

                stno=eval(self.student_no.get())
                mc.execute('SELECT student_no FROM student')
                stlist=[]
                for stu_no in mc:
                    stlist.append(stu_no[0])


                if stno in stlist:
                    messagebox.showinfo('Warning!','Student Number already exists')
                    self.student_no.set('')
                    self.stdno_entry.focus()
                    
                else:
                    sqlFormula=('INSERT INTO student (student_no,First_Name,Middle_Name,Last_Name,Father_Name,Mother_Name,course,branch,dob,mob,gender,email,blood_group,year,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                    student_info=(stno,self.first_name.get(),self.middle_name.get(),self.last_name.get(),self.father_name.get(),self.mother_name.get(),'BTECH',self.branch.get(),self.dob.get(),self.mob_no.get(),self.gender.get(),self.email.get(),self.blood_group.get(),self.year.get(),self.address.get())
                    mc.execute(sqlFormula,student_info)
                    mydb.commit()

                    candidate_Save_formula=('INSERT INTO login(username,password,actor) VALUES (%s,%s,%s)')
                    candidate_info=(str(stno),str(stno),'stu')
                    mc.execute(candidate_Save_formula,candidate_info)
                    mydb.commit()

                    messagebox.showinfo('Greets!','Data Sucsessfully saved')        
                    self.student_no.set('')
                    self.first_name.set('')
                    self.middle_name.set('')
                    self.last_name.set('')
                    self.father_name.set('')
                    self.mother_name.set('')
                    self.stdcourse_entry.config(text='')
                    self.branch.set('')
                    self.dob.set('')
                    self.mob_no.set('')
                    self.gender.set('')
                    self.email.set('')
                    self.blood_group.set('')
                    self.address.set('')
                    self.stdno_entry.focus()

                    
        def search_marks(self):

            if self.student1_no.get()=='':
                messagebox.showerror('Alert!','Entry is empty!')
            else:
                self.modify_flag=1
                if self.username=='stu':
                    form=('SELECT COUNT(*) FROM st1 WHERE Stdno=%s')
                    mc.execute(form,(eval(self.student1_no.get()),))

                else:
                    form=('SELECT COUNT(*) FROM st1 WHERE Stdno=%s and year=%s')
                    mc.execute(form,(eval(self.student1_no.get()),self.year.get()))


                for row in mc:
                     pass
                if row[0]>0:
                    formula=('SELECT * FROM student WHERE Student_no=%s')
                    mc.execute(formula,(eval(self.student1_no.get()),))
                    for info in mc:
                        
                        self.name1.set('{} {} {}'.format(info[1],info[2],info[3]))
                        self.marksbranch.set(info[7])


                    formula=('SELECT * FROM st1 WHERE Stdno=%s and year =%s')
                    mc.execute(formula,(eval(self.student1_no.get()),self.year.get(),))

                    for j in mc:
                        pass
                    if self.year.get()=="I":
                        if j[9]=="CSE":
                            self.sub1='KCS-101'
                            self.sub2='KCS-102'
                            self.sub3='KCS-103'
                            self.sub4='KCS-011'
                            self.sub5='KCS-015'
                            self.sub6='KNC'
                        elif j[9]=="IT":
                            self.sub1='KIT-101'
                            self.sub2='KIT-102'
                            self.sub3='KIT-103'
                            self.sub4='KIT-014'
                            self.sub5='KIT-018'
                            self.sub6='KNC'
                        elif j[9]=="ME":
                            self.sub1='KME-101'
                            self.sub2='KME-102'
                            self.sub3='KME-103'
                            self.sub4='KME-012'
                            self.sub5='KME-013'
                            self.sub6='KNC'
                        elif j[9]=="EC":
                            self.sub1='KEC-101'
                            self.sub2='KEC-102'
                            self.sub3='KEC-103'
                            self.sub4='KEC-017'
                            self.sub5='KEC-016'
                            self.sub6='KNC'
                        elif j[9]=="EN":
                            self.sub1='KEN-101'
                            self.sub2='KEN-102'
                            self.sub3='KEN-103'
                            self.sub4='KEN-011'
                            self.sub5='KEN-015'
                            self.sub6='KNC'
                        elif j[9]=="CE":
                            self.sub1='KCE-101'
                            self.sub2='KCE-102'
                            self.sub3='KCE-103'
                            self.sub4='kCE-013'
                            self.sub5='KCE-014'
                            self.sub6='KNC'
                        elif j[9]=="EI":
                            self.sub1='KEI-101'
                            self.sub2='KEI-102'
                            self.sub3='KEI-103'
                            self.sub4='kEI-011'
                            self.sub5='KEI-015'
                            self.sub6='KNC'




                    if self.year.get()=="II":
        
                        if j[9]=="CSE":
                            self.sub1='KCS-301'
                            self.sub2='KCS-302'
                            self.sub3='KCS-303'
                            self.sub4='KCS-031'
                            self.sub5='KCS-035'
                            self.sub6='KNC'
                        elif j[9]=="IT":
                            self.sub1='KIT-301'
                            self.sub2='KIT-302'
                            self.sub3='KIT-303'
                            self.sub4='KIT-034'
                            self.sub5='KIT-038'
                            self.sub6='KNC'
                        elif j[9]=="ME":
                            self.sub1='KME-301'
                            self.sub2='KME-302'
                            self.sub3='KME-303'
                            self.sub4='KME-033'
                            self.sub5='KME-036'
                            self.sub6='KNC'
                        elif j[9]=="EC":
                            self.sub1='KEC-301'
                            self.sub2='KEC-302'
                            self.sub3='KEC-303'
                            self.sub4='KEC-031'
                            self.sub5='KEC-035'
                            self.sub6='KNC'
                        elif j[9]=="EN":
                            self.sub1='KEN-301'
                            self.sub2='KEN-302'
                            self.sub3='KEN-303'
                            self.sub4='KEN-031'
                            self.sub5='KEN-035'
                            self.sub6='KNC'
                        elif j[9]=="CE":
                            self.sub1='KCE-301'
                            self.sub2='KCE-302'
                            self.sub3='KCE-303'
                            self.sub4='KCE-031'
                            self.sub5='KCE-035'
                            self.sub6='KNC'
                        elif j[9]=="EI":
                            self.sub1='KEI-301'
                            self.sub2='KEI-302'
                            self.sub3='KEI-303'
                            self.sub4='kEI-031'
                            self.sub5='KEI-035'
                            self.sub6='KNC'



                    if self.year.get()=="III":
        
                        if j[9]=="CSE":
                            self.sub1='KCS-501'
                            self.sub2='KCS-502'
                            self.sub3='KCS-503'
                            self.sub4='KCS-051'
                            self.sub5='KCS-055'
                            self.sub6='KNC'
                        elif j[9]=="IT":
                            self.sub1='KIT-501'
                            self.sub2='KIT-502'
                            self.sub3='KIT-503'
                            self.sub4='KIT-054'
                            self.sub5='KIT-058'
                            self.sub6='KNC'
                        elif j[9]=="ME":
                            self.sub1='KME-501'
                            self.sub2='KME-502'
                            self.sub3='KME-503'
                            self.sub4='KME-051'
                            self.sub5='KME-055'
                            self.sub6='KNC'
                        elif j[9]=="EC":
                            self.sub1='KEC-501'
                            self.sub2='KEC-502'
                            self.sub3='KEC-503'
                            self.sub4='KEC-051'
                            self.sub5='KEC-055'
                            self.sub6='KNC'
                        elif j[9]=="EN":
                            self.sub1='KEN-501'
                            self.sub2='KEN-502'
                            self.sub3='KEN-503'
                            self.sub4='KEN-051'
                            self.sub5='KEN-055'
                            self.sub6='KNC'
                        elif j[9]=="CE":
                            self.sub1='KCE-501'
                            self.sub2='KCE-502'
                            self.sub3='KCE-503'
                            self.sub4='KCE-051'
                            self.sub5='KCE-057'
                            self.sub6='KNC'
                        elif j[9]=="EI":
                            self.sub1='KEI-501'
                            self.sub2='KEI-502'
                            self.sub3='KEI-503'
                            self.sub4='kEI-051'
                            self.sub5='KEI-055'
                            self.sub6='KNC'



                    if self.year.get()=="IV":
        
                        if j[9]=="CSE":
                            self.sub1='KCS-701'
                            self.sub2='KCS-702'
                            self.sub3='KCS-703'
                            self.sub4='KCS-071'
                            self.sub5='KCS-075'
                            self.sub6='KNC'
                        elif j[9]=="IT":
                            self.sub1='KIT-701'
                            self.sub2='KIT-702'
                            self.sub3='KIT-703'
                            self.sub4='KIT-074'
                            self.sub5='KIT-078'
                            self.sub6='KNC'
                        elif j[9]=="ME":
                            self.sub1='KME-701'
                            self.sub2='KME-702'
                            self.sub3='KME-703'
                            self.sub4='KME-071'
                            self.sub5='KME-075'
                            self.sub6='KNC'
                        elif j[9]=="EC":
                            self.sub1='KEC-701'
                            self.sub2='KEC-702'
                            self.sub3='KEC-703'
                            self.sub4='KEC-071'
                            self.sub5='KEC-075'
                            self.sub6='KNC'
                        elif j[9]=="EN":
                            self.sub1='KEN-701'
                            self.sub2='KEN-702'
                            self.sub3='KEN-703'
                            self.sub4='KEN-071'
                            self.sub5='KEN-075'
                            self.sub6='KNC'
                        elif j[9]=="CE":
                            self.sub1='KCE-701'
                            self.sub2='KCE-702'
                            self.sub3='KCE-703'
                            self.sub4='KCE-071'
                            self.sub5='KCE-075'
                            self.sub6='KNC'
                        elif j[9]=="EI":
                            self.sub1='KEI-701'
                            self.sub2='KEI-702'
                            self.sub3='KEI-703'
                            self.sub4='kEI-071'
                            self.sub5='KEI-075'
                            self.sub6='KNC'



                
                    self.stno_entry.config(state=DISABLED)
                    
                    formula=('SELECT * FROM st1 WHERE Stdno=%s and year =%s')
                    mc.execute(formula,(eval(self.student1_no.get()),self.year.get(),))

                    
                    
                    for m in mc:
                        self.sub11=Label(self.framemarks,text=self.sub1,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub11.grid(row=1,column=0,padx=40,pady=15,sticky='w')
                        self.sub22=Label(self.framemarks,text=self.sub2,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub22.grid(row=2,column=0,padx=40,pady=15,sticky='w')
                        self.sub33=Label(self.framemarks,text=self.sub3,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub33.grid(row=3,column=0,padx=40,pady=15,sticky='w')
                        self.sub44=Label(self.framemarks,text=self.sub4,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub44.grid(row=4,column=0,padx=40,pady=15,sticky='w')
                        self.sub55=Label(self.framemarks,text=self.sub5,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub55.grid(row=5,column=0,padx=40,pady=15,sticky='w')
                        self.sub66=Label(self.framemarks,text=self.sub6,font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                        self.sub66.grid(row=6,column=0,padx=40,pady=15,sticky='w')

                        Label(self.framemarks,text='ST1',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=1,padx=80,pady=10,sticky='w')
                        Label(self.framemarks,text='ST2',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=2,padx=80,pady=10,sticky='w')
                        Label(self.framemarks,text='PUT',font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black').grid(row=0,column=3,padx=80,pady=10,sticky='w')


                        
                        
                        if m[2]=='ST1':
                            self.mm1=Label(self.framemarks,text=m[3],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm1.grid(row=1,column=1,padx=80,pady=5,sticky='w')
                            
                            self.mm2=Label(self.framemarks,text=m[4],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm2.grid(row=2,column=1,padx=80,pady=5,sticky='w')
                            
                            self.mm3=Label(self.framemarks,text=m[5],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm3.grid(row=3,column=1,padx=80,pady=5,sticky='w')
                            
                            self.mm4=Label(self.framemarks,text=m[6],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm4.grid(row=4,column=1,padx=80,pady=5,sticky='w')
                            
                            self.mm5=Label(self.framemarks,text=m[7],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm5.grid(row=5,column=1,padx=80,pady=5,sticky='w')
                            
                            self.mm6=Label(self.framemarks,text=m[8],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm6.grid(row=6,column=1,padx=80,pady=5,sticky='w')

                        if m[2]=='ST2':
                            self.mm1=Label(self.framemarks,text=m[3],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm1.grid(row=1,column=2,padx=80,pady=5,sticky='w')
                            
                            self.mm2=Label(self.framemarks,text=m[4],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm2.grid(row=2,column=2,padx=80,pady=5,sticky='w')
                            
                            self.mm3=Label(self.framemarks,text=m[5],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm3.grid(row=3,column=2,padx=80,pady=5,sticky='w')
                            
                            self.mm4=Label(self.framemarks,text=m[6],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm4.grid(row=4,column=2,padx=80,pady=5,sticky='w')
                            
                            self.mm5=Label(self.framemarks,text=m[7],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm5.grid(row=5,column=2,padx=80,pady=5,sticky='w')
                            
                            self.mm6=Label(self.framemarks,text=m[8],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm6.grid(row=6,column=2,padx=80,pady=5,sticky='w')

                        if m[2]=='PUT':
                            self.mm1=Label(self.framemarks,text=m[3],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm1.grid(row=1,column=3,padx=80,pady=5,sticky='w')
                            
                            self.mm2=Label(self.framemarks,text=m[4],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm2.grid(row=2,column=3,padx=80,pady=5,sticky='w')
                            
                            self.mm3=Label(self.framemarks,text=m[5],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm3.grid(row=3,column=3,padx=80,pady=5,sticky='w')
                            
                            self.mm4=Label(self.framemarks,text=m[6],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm4.grid(row=4,column=3,padx=80,pady=5,sticky='w')
                            
                            self.mm5=Label(self.framemarks,text=m[7],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm5.grid(row=5,column=3,padx=80,pady=5,sticky='w')
                            
                            self.mm6=Label(self.framemarks,text=m[8],font=('arial',15,' bold'),bd=0,relief=SOLID,bg='lightblue',fg='black')
                            self.mm6.grid(row=6,column=3,padx=80,pady=5,sticky='w')

                    if self.actor !='stu':
                        Button(self.framemarks,text='Clear',font=('arial',13,' bold'),bd=3,bg='lightblue',fg='black',command=self.clear_search_marks).place(x=650,y=390)
                        
                else:
                    messagebox.showinfo('Alert!','Sorry no record found!')




                    

        def find_search(self):
            if self.student1_no.get()=='':
                messagebox.showerror('Alert!','Entry is empty!')
            else:
                self.modify_flag=1
                if self.actor == 'stu':
                    form=('SELECT COUNT(*) FROM student WHERE Student_no=%s')
                    mc.execute(form,(eval(self.student1_no.get()),))
                else:
                    form=('SELECT COUNT(*) FROM student WHERE Student_no=%s and year=%s')
                    mc.execute(form,(eval(self.student1_no.get()),self.year.get()))

                for row in mc:
                     pass
                    
                if row[0]>0:
                    formula=('SELECT * FROM student WHERE Student_no=%s')
                    mc.execute(formula,(eval(self.student1_no.get()),))
                    

                    for info in mc:                        
                        self.name1.set('{} {} {}'.format(info[1],info[2],info[3]))                    
                        self.father1_name.set(info[4])
                        self.mother1_name.set(info[5])
                        self.course1.set(info[6])
                        self.branch1.set(info[7])
                        self.dob1.set(info[8])
                        self.mob1_no.set(info[9])
                        self.gender1.set(info[10])
                        self.email1.set(info[11])
                        self.blood1_group.set(info[12])
                        self.address1.set(info[14])                        
                        
                else:
                    messagebox.showinfo('Alert!','Sorry no record found!')




        def find_modify(self):
            if self.student1_no.get()=='':
                messagebox.showerror('Alert!','Entry is empty!')
            else:
                
                form=('SELECT COUNT(*) FROM student WHERE Student_no=%s and year=%s')
                mc.execute(form,(eval(self.student1_no.get()),self.year.get(),))

                for row in mc:
                     pass
                if row[0]>0:

                    self.stno_entry.destroy()
                    self.name11.destroy()
                    self.name22.destroy()
                    self.name33.destroy()
                    self.course11.destroy()
                    self.branch11.destroy()
                    self.DOB.destroy()
                    self.MOB.destroy()
                    self.gen.destroy()
                    self.email11.destroy()
                    self.father.destroy()
                    self.mother.destroy()
                    self.address.destroy()
                    self.blood.destroy()

                    self.stno=Label(self.frame2,textvariable=self.student1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='lightblue',fg='black',width=9,anchor='w')
                    self.stno.place(x=235,y=40)

                    self.name11_entry=Entry(self.frame2,textvariable=self.first_name,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black',width=9)
                    self.name11_entry.grid(row=0,column=3,pady=40,sticky='w')
                    
                    self.name22_entry=Entry(self.frame2,textvariable=self.middle_name,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black',width=9)
                    self.name22_entry.place(x=847,y=40,height=30)
                    
                    self.name33_entry=Entry(self.frame2,textvariable=self.last_name,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black',width=9)
                    self.name33_entry.place(x=955,y=40,height=30)
                    
                    self.course11_entry=Label(self.frame2,text='BTECH',font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black',width=18,anchor='w')
                    self.course11_entry.grid(row=1,column=1,padx=15,pady=20)
                    
                    self.branch11_entry=Entry(self.frame2,textvariable=self.branch1,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.branch11_entry.grid(row=1,column=3,pady=20,sticky='w')
                    
                    self.DOB_entry=Entry(self.frame2,textvariable=self.dob1,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.DOB_entry.grid(row=2,column=1,padx=15,pady=40,sticky='w')
                    
                    self.MOB_entry=Entry(self.frame2,textvariable=self.mob1_no,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.MOB_entry.grid(row=2,column=3,pady=20,sticky='w')
                    
                    self.gen_entry=Entry(self.frame2,textvariable=self.gender1,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.gen_entry.grid(row=3,column=1,padx=15,pady=20,sticky='w')
                    
                    self.email11_entry=Entry(self.frame2,textvariable=self.email1,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.email11_entry.grid(row=3,column=3,pady=20,sticky='w')
                    
                    self.father_entry=Entry(self.frame2,textvariable=self.father1_name,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.father_entry.grid(row=4,column=1,padx=15,pady=40,sticky='w')
                    
                    self.mother_entry=Entry(self.frame2,textvariable=self.mother1_name,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.mother_entry.grid(row=4,column=3,pady=40,sticky='w')
                    
                    self.address_entry=Entry(self.frame2,textvariable=self.address1,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.address_entry.grid(row=5,column=1,padx=15,pady=20,sticky='w')
                    
                    self.blood_entry=Entry(self.frame2,textvariable=self.blood1_group,font=('arial',15,' bold'),bd=2,relief=SUNKEN,bg='white',fg='black')
                    self.blood_entry.grid(row=5,column=3,pady=20,sticky='w')

                    formula=('SELECT * FROM student WHERE Student_no=%s')
                    mc.execute(formula,(eval(self.student1_no.get()),))
                    

                    for info in mc:
                        
                        #*********** modifystudent page **********
                        self.first_name.set(info[1])
                        self.middle_name.set(info[2])
                        self.last_name.set(info[3])
                       
                        self.father1_name.set(info[4])
                        self.mother1_name.set(info[5])
                        self.branch1.set(info[7])
                        self.dob1.set(info[8])
                        self.mob1_no.set(info[9])
                        self.gender1.set(info[10])
                        self.email1.set(info[11])
                        self.blood1_group.set(info[12])
                        self.address.set(info[14])

                        
                        
                else:
                    messagebox.showinfo('Alert!','Sorry no record found!')

                                
    def call(username,actor):
        root=Tk()
        obj=sms(root,username,actor)
        root.mainloop()

    

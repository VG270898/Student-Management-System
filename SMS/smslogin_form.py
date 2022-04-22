from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import datetime
import time
import os
import mysql.connector
################ LOCAL HOST MYSQL DATABASE CONNECTION #########################

u=''
a=''
f=False


try:
    '''mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='vishalgupta',
        database='sms'
        )'''

    mydb=mysql.connector.connect(
        host='b34hlxjqjbpnwinxud9w-mysql.services.clever-cloud.com',
        user='u6haifwrupocxuc7',
        password='zYNzWRRrXtiHyeugOaT8',
        database='b34hlxjqjbpnwinxud9w'
        )

    mc=mydb.cursor()

except:
    messagebox.showinfo('Connectivity Problem','Internet Issue\nor\nDatabase does not exixts')
    
else:

    class loginform:
        def __init__(self,root1):
            mydb.commit()
            self.root1=root1
            height = self.root1.winfo_screenheight() 
            width = self.root1.winfo_screenwidth()
            print(width,int(width/8),height,int(height/10))


            self.root1.geometry('1000x600+{}+{}'.format(int(width/8),int(height/12)))

            self.root1.title('Login Form')
            self.root1.resizable(0,0)
            self.root1.iconbitmap('smslogo.ico')
            self.root1.configure(background='#00B050')

            #**********VARIABLES*****************

            self.user=StringVar()
            self.password=StringVar()
            self.new_password=StringVar()
            

            self.img3=Image.open('title.png')
            self.img3=self.img3.resize((680,70),Image.ANTIALIAS)
            self.img3=ImageTk.PhotoImage(self.img3)

            self.img4=Image.open('credit.png')
            self.img4=self.img4.resize((650,40),Image.ANTIALIAS)
            self.img4=ImageTk.PhotoImage(self.img4)

            self.img5=Image.open('ADMIN_LOGIN_TITLE.png')
            self.img5=self.img5.resize((540,420),Image.ANTIALIAS)
            self.img5=ImageTk.PhotoImage(self.img5)

            self.img6=Image.open('STUDENT_LOGIN_TITLE.png')
            self.img6=self.img6.resize((540,420),Image.ANTIALIAS)
            self.img6=ImageTk.PhotoImage(self.img6)

            self.img7=Image.open('loginbutton.png')
            self.img7=self.img7.resize((370,43),Image.ANTIALIAS)
            self.img7=ImageTk.PhotoImage(self.img7)

            self.img8=Image.open('back.png')
            self.img8=self.img8.resize((45,43),Image.ANTIALIAS)
            self.img8=ImageTk.PhotoImage(self.img8)
            
            self.img9=Image.open('reset_pass.png')
            self.img9=self.img9.resize((370,43),Image.ANTIALIAS)
            self.img9=ImageTk.PhotoImage(self.img9)

            self.img10=Image.open('FORGOT_FRAME.png')
            self.img10=self.img10.resize((540,420),Image.ANTIALIAS)
            self.img10=ImageTk.PhotoImage(self.img10)



            self.img1=Image.open('admin.png')
            self.img1=self.img1.resize((400,150),Image.ANTIALIAS)
            self.img=ImageTk.PhotoImage(self.img1)

            self.img2=Image.open('student.png')
            self.img2=self.img2.resize((400,150),Image.ANTIALIAS)
            self.img21=ImageTk.PhotoImage(self.img2)

    ##################### TITLE BAR ##################################################
            title=Label(self.root1,image=self.img3,bg='#00B050').pack()
            

    ##################### MAIN FRAME ###################################################
    ########################### CREDIT BAR ##########################################
            credit=Label(self.root1,image=self.img4,bg='#00B050')
            credit.pack(padx=45,pady=10,side=BOTTOM)

            self.verified=StringVar()

            self.mainpage()
            

        def callback(self,event,actor,action):
            print(event)
            if action==11:
                if event.widget.get()=='Username':
                    event.widget.delete(0,END)
                    if actor=='adm':
                        self.adm_username_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    elif actor=='rst':
                        self._username_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    else:
                        self.stu_username_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    
                    
            if action==12:
                if event.widget.get()=='':
                    if actor=='adm':
                        self.user.set('Username')
                        self.adm_username_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')
                    elif actor=='rst':
                        self.user.set('Username')
                        self._username_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')
                    else:
                        self.user.set('Username')
                        self.stu_username_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')

            if action==21:
                if event.widget.get()=='Password' or event.widget.get()=='New Password':
                    event.widget.delete(0,END)
                    if actor=='adm':
                        self.adm_password_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    elif actor=='rst':
                        self.new_password_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    else:
                        self.stu_password_entry.config(font=('Constantia','15','bold'),fg='#262626')
                    
                    
                
            if action==22:
                if event.widget.get()=='':
                    if actor=='adm':
                        self.password.set('Password')
                        self.adm_password_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')
                    if actor=='rst':
                        self.new_password.set('New Password')
                        self.new_password_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')
                    else:
                        self.password.set('Password')
                        self.stu_password_entry.config(font=('BankGothic LT BT','16','bold'),fg='#A6A6A6')
                

                
            
            
        def back_to_mainpage(self):
            self.frame.destroy()
            self.mainpage()
            
        def mainpage(self):

            self.frame=Frame(self.root1,bd=3,relief=SUNKEN,bg='#00B050')
            self.frame.pack(fill=BOTH,expand=1,padx=20)

            ####################### ACTOR FRAME ##############################################
                        
            self.actor_frame=Frame(self.frame,bg='#00B050')
            self.actor_frame.pack(pady=50,fill=BOTH,expand=1)

            admin_button=Button(self.actor_frame,bg='#00B050',activebackground='#00B050',image=self.img,bd=0,command=lambda:self.admin_login_page())
            admin_button.pack(padx=35,pady=10,side=LEFT)
                
            student_button=Button(self.actor_frame,bg='#00B050',activebackground='#00B050',image=self.img21,bd=0,command=lambda:self.student_login_page())
            student_button.pack(padx=35,pady=10,side=RIGHT)



        def admin_login_page(self):
            self.actor_frame.destroy()

            back_button=Button(self.frame,image=self.img8,bg='#00B050',bd=0,command=lambda:self.back_to_mainpage(),activebackground='#00B050')
            back_button.place(x=10,y=10)
            
            admin_loginFrame=Label(self.frame,image=self.img5,bg='#00B050')
            admin_loginFrame.pack(pady=10)
            
            self.user.set('Username')

            self.adm_username_entry=Entry(self.frame,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.user)
            self.adm_username_entry.place(x=295,y=230,height=30,width=364)
            
            self.adm_username_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='adm',action=11))
            self.adm_username_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='adm',action=12))


            self.password.set('Password')
            
            self.adm_password_entry=Entry(self.frame,width=21,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.password)
            self.adm_password_entry.place(x=295,y=280,height=30,width=364)

            self.adm_password_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='adm',action=21))
            self.adm_password_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='adm',action=22))


            self.adm_login_button=Button(self.frame,image=self.img7,bg='#00BE50',activebackground='#00BE50',bd=0,command=lambda:self.verify('adm'))
            self.adm_login_button.place(x=290,y=325)
            

            self.forgot_pass=Button(self.frame,text='Forgot Password',command=lambda:self.forgot(),font=('BankGothic LT BT','10'),bg='#00BE50',activebackground='#00BE50',bd=0).place(x=407,y=380)


        def student_login_page(self):
            self.actor_frame.destroy()
            

            back_button=Button(self.frame,image=self.img8,bg='#00B050',bd=0,command=lambda:self.back_to_mainpage(),activebackground='#00B050')
            back_button.place(x=10,y=10)


            student_loginFrame=Label(self.frame,image=self.img6,bg='#00B050')
            student_loginFrame.pack(pady=10)
            
            self.user.set('Username')

            self.stu_username_entry=Entry(self.frame,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.user)
            self.stu_username_entry.place(x=295,y=230,height=30,width=364)

            self.stu_username_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='stu',action=11))
            self.stu_username_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='stu',action=12))

            
            self.password.set('Password')
            
            self.stu_password_entry=Entry(self.frame,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.password)
            self.stu_password_entry.place(x=295,y=280,height=30,width=364)

            self.stu_password_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='stu',action=21))
            self.stu_password_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='stu',action=22))


            self.stu_login_button=Button(self.frame,image=self.img7,bg='#00BE50',activebackground='#00BE50',bd=0,command=lambda:self.verify('stu'))
            self.stu_login_button.place(x=290,y=325)



            self.forgot_pass=Button(self.frame,text='Forgot Password',command=lambda:self.forgot(),font=('BankGothic LT BT','10'),bg='#00BE50',activebackground='#00BE50',bd=0).place(x=407,y=380)
            
                

        def verify(self,actor):
            global u,a,f

            print(actor,type(actor))
            self.verified.set('')
            formula_stu=('SELECT count(*) FROM login WHERE username=%s and password=%s and actor=%s')
            mc.execute(formula_stu,(self.user.get(),self.password.get(),actor,))

            for i in mc:
                pass
            print(i)
                
            if i[0]>0:
                self.verified.set('Successfully Verified')
                
                formula_stu=('SELECT * FROM login WHERE username=%s and password=%s and actor=%s')
                mc.execute(formula_stu,(self.user.get(),self.password.get(),actor,))

                for j in mc:
                    pass
                print(j)

                u=j[0]
                a=j[2]
                f=True
                    
                self.root1.destroy()
                
            else:
                self.verified.set('Warning! Wrong Username or Password')
                self.invalid=Label(self.frame,textvariable=self.verified,font=('BankGothic LT BT','10'),fg='black',bg='yellow',bd=0)
                self.invalid.place(x=335,y=210)
                 
                 
        def forgot(self):
            self.frame.destroy()
            self.frame=Frame(self.root1,bd=3,relief=SUNKEN,bg='#00B050')
            self.frame.pack(fill=BOTH,expand=1,padx=20)
            
            back_button=Button(self.frame,image=self.img8,bg='#00B050',bd=0,command=lambda:self.back_to_mainpage(),activebackground='#00B050')
            back_button.place(x=10,y=10)

            forgot_password_frame=Label(self.frame,image=self.img10,bg='#00B050')
            forgot_password_frame.pack(pady=10)

            self.user.set('Username')

            self._username_entry=Entry(self.frame,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.user)
            self._username_entry.place(x=295,y=230,height=30,width=364)

            self._username_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='rst',action=11))
            self._username_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='rst',action=12))

            
            self.new_password.set('New Password')
            
            self.new_password_entry=Entry(self.frame,font=('BankGothic Md BT','16','bold'),fg='#A6A6A6',bd=2,relief=SUNKEN,textvariable=self.new_password)
            self.new_password_entry.place(x=295,y=280,height=30,width=364)

            self.new_password_entry.bind("<FocusIn>", lambda event:self.callback(event,actor='rst',action=21))
            self.new_password_entry.bind("<FocusOut>", lambda event:self.callback(event,actor='rst',action=22))


            self.stu_login_button=Button(self.frame,image=self.img9,bg='#00BE50',activebackground='#00BE50',bd=0,command=lambda:self.reset_func())
            self.stu_login_button.place(x=290,y=325)
            

            
        def reset_func(self):
                            
            try:
                formula_forgot=('SELECT count(*) FROM login WHERE username=%s')
                mc.execute(formula_forgot,(self.user.get(),))

                for i in mc:
                    pass
                    
                if i[0]>0:
                    print(self.new_password.get())
                    if self.new_password.get()=='' or self.new_password.get()=='New Password':
                        messagebox.showinfo('Warning','Enter correct Password!')
                    else:
                        formula_reset=('UPDATE login SET password=%s WHERE username=%s')
                        mc.execute(formula_reset,(self.new_password.get(),self.user.get(),))
                        mydb.commit()

                        messagebox.showinfo('Information','Successfully Password Reset')
                        self.back_to_mainpage()
                else:
                    self._username_entry.focus()
                    
                    messagebox.showinfo('Warning','Username not exists!')
            except:
                messagebox.showerror('Error','Something went wrong!')


    
    def authenticate():
        global u,a,f
        root1=Tk()
        u=''
        a=''
        f=False
        ob=loginform(root1)
        root1.mainloop()
        return u,a,f
        
        
    
        


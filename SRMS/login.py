from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import os

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #======bg image=====
        self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #==========frames========================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        #=======labels===========================

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#1C1C1C").place(x=270,y=50)
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=240,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=240,y=180,width=350,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=240,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=240,y=280,width=350,height=35)
        #========buttons===========
        btn_reg=Button(login_frame,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=235,y=320)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=240,y=380,width=180,height=40)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from user where email=? and password =?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Login Successful",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root=Tk()
obj=login(root)
root.mainloop()
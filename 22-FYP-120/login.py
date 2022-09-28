from tkinter import *
from turtle import color
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib.pyplot import title
import pymysql

class page_login:
    def __init__(self,window):
        self.window = window
        window.title('Login Panel')
        self.window.geometry("1366x768")
        self.window.state('zoomed')
        
        # =======================================================================================
        # ===========================  BACKGROUND IMAGE  ========================================
        # =======================================================================================

        win_icon = ImageTk.PhotoImage(file = "images/window_icon.ico")
        self.window.iconphoto(True,win_icon)
        
        self.background_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        bg_image = Label(self.window , image=self.background_image)
        bg_image.place(x=0, y=0, width=1366)
        
        # =======================================================================================
        # =================================  Header  ============================================
        # =======================================================================================



        title = Label(self.window, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28,"bold"), bg="#5780B6", fg="lightgray")
        title.place(x=0 , y=3, width=1366, height=90)

        # =====================================================================================================
        # ============================================  BODY  =================================================
        # =====================================================================================================

        # =============  LOGIN FORM  =============
        
        frame_Login = Frame(self.window, bg="#5780B6")
        frame_Login.place(x=830, y=180, width=480, height=480)

        title_frame = Label(frame_Login, text="LOGIN HERE ..",font=("Impact",24), fg="lightgray", bg="#5780B6")
        title_frame.place(x=50, y=30)
        desc_frame = Label(frame_Login, text="Admin / Worker Login Area",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6")
        desc_frame.place(x=60, y=100)

        # ====================================  TEXTBOX ENTRIES
        
        # ===============  ROW-1 USER EMAIL ENTRY
        lbl_user = Label(frame_Login, text="User ID/Email",font=("Goudy old style",14), fg="lightgray", bg="#5780B6")
        lbl_user.place(x=70, y=140)
        self.txt_user = Entry(frame_Login, font=("times new roman",16),fg="black",bg="lightgray")
        self.txt_user.place(x=70, y=170, height=35, width=350)

        # ===============  ROW-2 USER PASSWORD ENTRY
        lbl_pass = Label(frame_Login, text="Password",font=("Goudy old style",15), fg="lightgray", bg="#5780B6")
        lbl_pass.place(x=70, y=210)
        self.txt_pass = Entry(frame_Login, font=("times new roman",15), fg="black",bg="lightgray", show='*')
        self.txt_pass.place(x=70, y=240, height=35, width=350)

        # ===============  ROW-3 FORGET AND SHOW PASSWORD BUTTON ENTRY
        show_password = Checkbutton(frame_Login, text='Show Password', command=self.show_password, font=("times new roman",13),fg="lightgray",  bg="#5780B6")
        show_password.place(x=70 , y=280)
        forget_btn = Button(frame_Login, text="Forget Password? Click Here ....", command=self.Forget_Password, bg="#5780B6", fg="lightgray", activebackground="#5780B6",activeforeground="white", bd=0, font=("times new roman", 13))
        forget_btn.place(x=70, y=310)
        
        # ===============  LOGIN ENTRY

        login_btn = Button(frame_Login, text="Login", command=self.login, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("calibri",20))
        login_btn.place(x=70, y=370, height=50, width=160)
        
        register_btn = Button(frame_Login, text="Register", command=self.register_window, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("calibri",20))
        register_btn.place(x=260, y=370 , height=50, width=160)
        # ===============  REGISTER BUTTON ENTRY
       
# #C6C4C5
    # =====================================================================================================
    # =====================================  BACKEND CODDING  =============================================
    # =====================================================================================================
    
    # ==========================  REGISTER WINDOW FUNCTION
    def register_window(self):
        window.destroy()
        import register

    # ========================== DASHBOARD WINDOW FUNCTION
    def Dashboard_page(self):
        window.destroy()
        import Worker_Dashboard

    # ========================== FORGET WINDOW FUNCTION
    def Forget_Password(self):
        #window.destroy()
        import Change_Password

    # ========================== SHOW PASSWORD FUNCTION    
    def show_password(self):
        if self.txt_pass.cget('show') == '*':
            self.txt_pass.config(show='')
        else:
            self.txt_pass.config(show='*')

    # ========================== LOGIN USING DATABASE FUNCTION
    def login(self):
        if self.txt_user.get() == "" and self.txt_pass.get() == "":
            messagebox.showerror("ERROR","All Feilds are required" , parent = self.window)
        
        elif self.txt_user.get() == "talha@gmail.com" and self.txt_pass.get() == "Talha123":
            messagebox.showinfo("Success","Admin Login Successfull",parent = self.window)
            self.window.destroy()
            import Admin_Dashboard
        

        else:
            try:
                con = pymysql.connect(host="localhost" , user="root" , password="" , database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from register_login where email = %s and password = %s", (self.txt_user.get(),self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Email & Password" , parent=self.window)
                else:
                    messagebox.showinfo("Success", "Login Successfull", parent=self.window)
                    self.Dashboard_page()
                con.close()
                
            except Exception as es:
                messagebox.showerror("Error" , f"Error due to: {str(es)}" , parent=self.window)



window = Tk()
obj = page_login(window)
window.mainloop()
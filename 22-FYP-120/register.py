# =======================================================================================
# ===========================  INCLUDED LIBRARIES  ========================================
# =======================================================================================

from tkinter import *
from turtle import bgcolor, color
from PIL import Image, ImageTk
from tkinter import messagebox , ttk
from matplotlib.pyplot import title
import pymysql
import re

# =======================================================================================
# ===========================  WINDOW DETAILS  ========================================
# =======================================================================================

class page_register:
    def __init__(self,window):
        self.window = window
        window.title('REGISTRATION')
        self.window.geometry("1366x768")
        self.window.state('zoomed')

        # window icon 
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.window.iconphoto(True, win_icon)

        # =======================================================================================
        # =================================  Header  ============================================
        # =======================================================================================

        title = Label(self.window, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28,"bold"), bg="#5780B6", fg="lightgray")
        title.place(x= 0, y= 0, width=1366, height=90)

        # =====================================================================================================
        # ============================================  BODY  =================================================
        # =====================================================================================================

        # =================  LEFT IMAGE  
        self.left_image = ImageTk.PhotoImage(file = "images/11.jpeg")
        left = Label(self.window, image=self.left_image)
        left.place(x=130, y=150, height=500, width=400)

        # ======================================  REGISTRATION FORM  ==========================================

        frame_Register = Frame(self.window, bg="#5780B6")
        frame_Register.place(x=530, y=150, width=700, height=500)

        title_frame = Label(frame_Register, text="REGISTER HERE ....", font=("times new roman",26,"bold"),bg="#5780B6",fg="lightgray")
        title_frame.place(x=50, y=30)

        # ====================================  TEXTBOX ENTRIES

        # ===============  ROW-1 FIRST NAME ENTRY 
        user_id = Label(frame_Register, text="Name", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=50, y=100)
        self.txt_name = Entry(frame_Register, font=("times new roman",15), bg="lightgray")
        self.txt_name.place(x=50, y=130, width=250)
        
        # ===============  ROW-1 LAST NAME ENTRY 
        u_name = Label(frame_Register, text="User Name", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=370, y=100)
        self.txt_uname = Entry(frame_Register,font=("times new roman",15), bg="lightgray")
        self.txt_uname.place(x=370, y=130, width=250)

        # ===============  ROW-2 CONTACT ENTRY 
        contact = Label(frame_Register, text="Contact No. ", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=50, y=170)
        self.txt_contact = Entry(frame_Register,font=("times new roman",15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        # ===============  ROW-2 EMAIL ENTRY 
        email = Label(frame_Register, text="Email", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=370, y=170)
        self.txt_email = Entry(frame_Register,font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
        
        # ===============  ROW-3 SECURITY QUESTION ENTRY 
        question = Label(frame_Register, text="Security Question", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame_Register,font=("times new roman",13), state="readonly", justify=CENTER, foreground="black")
        self.cmb_quest['values'] = ("Select","What is your Pet Name","What is your Friend Name","Which feild you like most" )
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        # ===============  ROW-3 ANSWER ENTRY 
        answer = Label(frame_Register, text="Answer", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=370, y=240)
        self.txt_answer = Entry(frame_Register,font=("times new roman",15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)
        
        # ===============  ROW-4 PASSWORD ENTRY 
        password = Label(frame_Register, text="Password", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=50, y=310)
        self.txt_pasword = Entry(frame_Register,font=("times new roman",15), bg="lightgray", show='*')
        self.txt_pasword.place(x=50, y=340, width=250)
        
        # ===============  ROW-4 CONFIRM PASSWORD ENTRY 
        cpassword = Label(frame_Register, text="Confirm Password", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame_Register,font=("times new roman",15), bg="lightgray", show='*')
        self.txt_cpassword.place(x=370, y=340, width=250)

        # ===============  ROW-5 CHECKBUTTON-SHOW PASSWORD ENTRY 
        show_password = Checkbutton(frame_Register, text='Show Password', command=self.show_password, font=("times new roman",13),fg="lightgray",  bg="#5780B6")
        show_password.place(x=50 , y=380)

        # =============== REGISTER BUTTON ENTRY 
        register_btn = Button(frame_Register, text="Register", command=self.register_data, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("calibri",22))
        register_btn.place(x=200, y=430, width=250)

        # ===============  LOGIN BUTTON ENTRY
        login = Label(self.window , text='If already registered please Login......' ,
        font=("calibri",18,"italic"),fg="lightgray", bg="#808CA4")
        login.place(x=150 , y=350 )
        btn_login = Button(self.window, text="Login", command=self.login_window, font=("calibri",20),  bg="lightgray", cursor="hand2")
        btn_login.place(x=240, y=420, width=180)

        self.special_char = ["@" and "."]
        # #C6C4C5

    # ==========================================================================================
    # ======================================  Validations  =====================================
    # ==========================================================================================
    
    # =====================================================================================================
    # =====================================  BACKEND CODDING  =============================================
    # =====================================================================================================

    # ========================== CLEAR ALL FEILDS FUNCTION
    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_uname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pasword.delete(0,END)
        self.txt_cpassword.delete(0,END)

    # ========================== SHOW PASSWORD FUNCTION
    def show_password(self):
        if self.txt_pasword.cget('show') == '*' or self.txt_cpassword.cget('show') == '*':
            self.txt_pasword.config(show = '') or self.txt_cpassword.config(show = '')
        else:
            self.txt_pasword.config(show='*') or self.txt_cpassword.config(show = '*')


    # ========================== LOGIN WINDOW FUNCTION
    def login_window(self):
        self.window.destroy()
        import login
    
    # ========================== REGISTER DATA TO DATABASE FUNCTION
    def register_data(self):
        if self.txt_name.get() == "" or self.txt_uname.get() == "" or self.txt_contact.get() =="" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() =="" or self.txt_pasword.get() =="" or self.txt_cpassword.get() =="":
            messagebox.showerror("Error", "All Feilds are Required", parent=self.window)
        elif any(ch.isdigit() for ch in self.txt_name.get()):
            messagebox.showerror("Error","Name can't have numbers", parent = self.window)
        elif not any(ch in self.special_char for ch in self.txt_email.get()):
            messagebox.showerror("Error","Incorrect Email Address")
        elif self.txt_pasword.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password must be same", parent = self.window)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from register_login where email=%s", self.txt_email.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Already Exist", parent=self.window)
                else:
                    cur.execute("insert into register_login (Name,username,contact,email,question,answer,password) values (%s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.txt_name.get(),
                                    self.txt_uname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_pasword.get()
                                )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfull", parent=self.window)
                    self.login_window()
                    self.clear()

            except Exception as es:
                messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.window)




window = Tk()
obj = page_register(window)
window.mainloop()
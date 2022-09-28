# =======================================================================================
# ===========================  INCLUDED LIBRARIES  ========================================
# =======================================================================================
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox , ttk
from matplotlib.pyplot import title
import pymysql
import re

# =======================================================================================
# ===========================  WINDOW DETAILS  ========================================
# =======================================================================================

class page_addupdate:
    def __init__(self,window):
        # window = tkinter.Toplevel()
        self.window = window
        window.title('Admin - Update')
        self.window.geometry("1366x768")
        self.window.resizable(False, False)

        # # ===========  WINDOW ICON  =============
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.window.iconphoto(True, win_icon)

        # =====================================================================================================
        # ============================================  BODY  =================================================
        # =====================================================================================================
        self.background_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        bg_image = Label(self.window , image=self.background_image)
        bg_image.place(x=0, y=0, width=1366)

        title = Label(self.window, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28), bg="#5780B6", fg="lightgray")
        title.place(x=0 , y=3, width=1366, height=90)
        back_btn = Button(self.window, text="Back", command=self.Back_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        back_btn.place(x=10, y=28)
       
        # Frama Register
        frame_Register = Frame(self.window, bg="#5780B6")
        frame_Register.place(x=620, y=120, width=680, height=600)

        # ======================================  REGISTRATION FORM  ==========================================

        title_frame = Label(frame_Register, text="ADD / UPDATE WORKERS HERE .....", font=("times new roman",22),bg="#5780B6",fg="lightgray")
        title_frame.place(x=50, y=30)

        # ====================================  TEXTBOX ENTRIES

        # ===============  ROW-1 FIRST NAME ENTRY 
        user_name = Label(frame_Register, text="Name", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=50, y=100)
        self.txt_name = Entry(frame_Register, font=("times new roman",15), bg="lightgray")
        self.txt_name.place(x=50, y=130, width=250)

        # ===============  ROW-1 LAST NAME ENTRY 
        u_name = Label(frame_Register, text="Username", font=("times new roman",15),bg="#5780B6",fg="lightgray").place(x=370, y=100)
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
        self.cmb_quest = ttk.Combobox(frame_Register,font=("times new roman",13), state="readonly", justify=CENTER)
        self.cmb_quest['values'] = ("Select","What is your Pet Name","What is your Friend Name","Which feild you like most")
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
        show_password.place(x=50 , y=400)

        # =============== ADD BUTTON ENTRY 
        btn_Add = Button(frame_Register, text="Add Worker", command=self.add_data, font=("calibri",16), fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", borderwidth=4, cursor="hand2")
        btn_Add.place(x=90, y=480, width=170)

        # =============== UPDATE BUTTON ENTRY 
        btn_Update = Button(frame_Register, text="Update Record", command=self.update_data, font=("calibri",16), fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", borderwidth=4, cursor="hand2")
        btn_Update.place(x=400, y=480, width=200)
        
        self.special_char = ["@","."]
    
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

    def Admin_Dashboard(self):
        window.destroy()
        import Admin_manage_User
    
    def Back_Func(self):
        window.destroy()
        import Admin_manage_User

    # =================== UPDATE Data Window FUNCTION   
    def update_data(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
            cur = con.cursor()
            cur.execute("UPDATE register_login SET Name = %s, username = %s,contact = %s,question = %s,answer = %s,password = %s WHERE email = %s",
                        (
                            self.txt_name.get(),
                            self.txt_uname.get(),
                            self.txt_contact.get(),
                            self.cmb_quest.get(),
                            self.txt_answer.get(),
                            self.txt_pasword.get(),
                            self.txt_email.get(),                    
                        )
                        )
            # con.commit()
            # con.close()
            messagebox.showinfo("Success", "Updated Successfull", parent=self.window)
            self.Admin_Dashboard()
               
                    
        except Exception as es:
            messagebox.showerror("Error", f"Error due to :  {str(es)}", parent=self.window)


    # =================== Add Data Window FUNCTION
    def add_data(self):
        if self.txt_name.get() == "" or self.txt_uname.get() == "" or self.txt_contact.get() =="" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() =="" or self.txt_pasword.get() =="" or self.txt_cpassword.get() =="":
            messagebox.showerror("Error", "All Feilds are Required", parent=self.window)
        elif any(ch.isdigit() for ch in self.txt_name.get()):
            messagebox.showerror("Error","Name can't have numbers", parent = self.window)
        elif not any(ch in self.special_char for ch in self.txt_email.get()):
            messagebox.showerror("Error","Incorrect Email Address")
        elif len(self.txt_pasword.get()) < 8 :
            messagebox.showerror("Error","Password must be minimum of 8 characters!",parent = window)
        elif self.txt_pasword.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password must be same", parent = self.window)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from register_login where email=%s", self.txt_email.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Success", "User Already Exist", parent=self.window)
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
                    # con.commit()
                    # con.close()
                    messagebox.showinfo("Success", "Register Successfull", parent=window)
                    self.Admin_Dashboard()

                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to :  {str(es)}", parent=self.window)


window = Tk()
obj = page_addupdate(window)
window.mainloop()
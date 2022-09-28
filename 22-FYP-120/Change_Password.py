from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from matplotlib.pyplot import title
import pymysql

class page_ChabgePassword:
    def __init__(self,fp):
        
        self.fp = fp
        fp.title('Change Password')
        self.fp.geometry("500x420+295+120")
        self.fp.resizable(False,False)
        # self.fp.configure(bg="#5780B6")

        
        Frame_FPass = Frame(fp, bg='#5780B6')
        Frame_FPass.place(x=0, y=0, height=410, width=490)
        Frame_FPass.place(anchor='center', relx=0.5, rely=0.5)

        # ====================================  TEXTBOX ENTRIES
        
        # ===============  Title Frame
        title_FP = Label(Frame_FPass, text='CHANGE PASSWORD HERE ....', font=("Calibri",25,"bold"), bg='#5780B6', fg="lightgray")
        title_FP.place(x=40 , y=20)

        # ===============  ROW-1 USER EMAIL ENTRY
        lbl_user = Label(Frame_FPass, text="User Email",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6")
        lbl_user.place(x=70, y=85)
        self.txt_user = Entry(Frame_FPass, font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=70, y=110, height=35, width=350)

        # ===============  ROW-2 USER PASSWORD ENTRY
        lbl_pass = Label(Frame_FPass, text="Password",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6")
        lbl_pass.place(x=70, y=155)
        self.txt_pass = Entry(Frame_FPass, font=("times new roman",15),bg="lightgray",  show='*')
        self.txt_pass.place(x=70, y=180, height=35, width=350)

        # ===============  ROW-3 USER NEW PASSWORD ENTRY
        lbl_npass = Label(Frame_FPass, text="New Password",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6")
        lbl_npass.place(x=70, y=225)
        self.txt_npass = Entry(Frame_FPass, font=("times new roman",15) ,bg="lightgray", show='*')
        self.txt_npass.place(x=70, y=250, height=35, width=350)

        # ===============  ROW-4 SHOW PASSWORD BUTTON ENTRY
        show_password = Checkbutton(Frame_FPass, text='Show Password', command=self.show_password, font=("times new roman",13),fg="lightgray",  bg="#5780B6")
        show_password.place(x=70 , y=295)
        
        # ===============  LOGIN ENTRY
        changepass_btn = Button(Frame_FPass, text="Change Password", command=self.change_pass, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("calibri",20))
        changepass_btn.place(x=140, y=345, height=40, width=220)
    
    # ========================== SHOW PASSWORD FUNCTION
    def show_password(self):
        if self.txt_pass.cget('show') or self.txt_npass.cget('show') == '*':
            self.txt_pass.config(show = '') or self.txt_npass.config(show = '')
        else:
            self.txt_pass.config(show='*') or self.txt_npass.config(show='*')

    def Login_Window(self):
        fp.destroy()
        import login

    def clear(self):
        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_npass.delete(0, END)

    def change_pass(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "" or self.txt_npass.get() == "" :
            messagebox.showerror("Error","All Feilds are required !!", parent = self.fp)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from register_login where email=%s", self.txt_user.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "User Not Exist", parent= self.fp)
                else:
                    cur.execute("UPDATE register_login SET password = %s WHERE email = %s",
                                (
                                    self.txt_npass.get(),
                                    self.txt_user.get(),
                                )
                            )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password Updated Successfully !!", parent = self.fp)
                    self.Login_Window()
                    self.clear()
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to :  {str(es)}", parent = self.fp)


fp = Tk()
obj = page_ChabgePassword(fp)
fp.mainloop()
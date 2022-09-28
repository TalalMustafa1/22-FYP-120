from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from matplotlib.pyplot import title
import pymysql

class page_ChabgePassword:
    def __init__(self,fp):
        
        self.fp = fp
        fp.title('Delete Worker')
        fp.geometry("500x420+295+120")
        fp.resizable(False,False)

        
        Frame_FPass = Frame(fp, bg='#5780B6')
        Frame_FPass.place(x=0, y=0, height=410, width=490)
        Frame_FPass.place(anchor='center', relx=0.5, rely=0.5)

        # ====================================  TEXTBOX ENTRIES
        
        # ===============  Title Frame
        title_FP = Label(Frame_FPass, text='Delete User HERE ....', font=("Calibri",25,"bold"), bg='#5780B6', fg="lightgray")
        title_FP.place(x=40 , y=20)

        # ===============  ROW-1 USER EMAIL ENTRY
        lbl_user = Label(Frame_FPass, text="User Email",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6")
        lbl_user.place(x=70, y=85)
        self.txt_useremail = Entry(Frame_FPass, font=("times new roman",15),bg="lightgray")
        self.txt_useremail.place(x=70, y=110, height=35, width=350)

        
        # ===============  LOGIN ENTRY
        changepass_btn = Button(Frame_FPass, text="Delete Worker", command=self.Delete_User, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("calibri",20))
        changepass_btn.place(x=140, y=345, height=40, width=220)
    
    # ========================== SHOW PASSWORD FUNCTION
    
    
    def clear(self):
        self.txt_useremail.delete(0, END)
    
    def AdminPanel_FUnc(self):
        fp.destroy()
        import Admin_manage_User
    
    def Delete_User(self):
        if self.txt_useremail.get() == "":
            messagebox.showerror("Error","All Feilds are required !!", parent = self.fp)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from register_login where email=%s", self.txt_useremail.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "User Not Exist", parent= self.fp)
                else:
                    cur.execute("DELETE from register_login WHERE email = %s",
                                (
                                    self.txt_useremail.get(),
                                )
                            )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Record Deleted Successfully !!", parent = self.fp)
                    self.AdminPanel_FUnc()
                    self.clear()
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to :  {str(es)}", parent = self.fp)


fp = Tk()
obj = page_ChabgePassword(fp)
fp.mainloop()
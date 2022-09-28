from tkinter import *
from tokenize import cookie_re
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class page_User:
    def __init__(self,root):
        self.root = root
        self.root.title("Manage Worker")
        self.root.geometry("1366x768")
        self.root.state("zoomed")

        # window icon 
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.root.iconphoto(True, win_icon)
        

        # =======================================================================================
        # ===========================  BACKGROUND IMAGE  ========================================
        # =======================================================================================

        self.back_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        backimage_label = Label(root, image=self.back_image)
        backimage_label.place(x=0, y=0 , width = 1366)
        # backimage_label.place(x=293, y=90, width=1073, height=750)

        # =======================================================================================
        # =================================  Header  ============================================
        # =======================================================================================

        title = Label(self.root, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28,"bold"), bg="#5780B6", fg="lightgray")
        title.place(x=0 , y=3, width=1366, height=90)
        back_btn = Button(self.root, text="Back", command=self.Back_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        back_btn.place(x=10, y=28)
        self.txt_logout = Button(self.root, text='Logout', command=self.Logout_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        self.txt_logout.place(x=1250, y=28)

        # --------------------------------------      Frame Set         ------------------------------------
        
        Frame_standrad = Frame(self.root, bg="#5780B6")
        Frame_standrad.place(x=981, y=190, height=450, width=260)

        Frame_table = Frame(self.root, bg="#5780B6")
        Frame_table.place(x=100, y=190, height=450, width=880)
        
        # -------------------------------------     Dashboard Area    -------------------------------
        
        add_btn = Button(Frame_standrad, text="Add User", command=self.AddUpdateUser_Func, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        add_btn.place(x=30, y=50, height=40, width=200)

        update_btn = Button(Frame_standrad, text="Update User", command=self.AddUpdateUser_Func, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        update_btn.place(x=30, y=150, height=40, width=200)

        delete_btn = Button(Frame_standrad, text="Delete User", command=self.DeleteUser_Func, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        delete_btn.place(x=30, y=250, height=40, width=200)

        
        # -------------------------------------    Table Generation   -------------------------------
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
            cur = con.cursor()
            cur.execute("SELECT * FROM register_login") 
            e=Label(Frame_table, width = 11, font=("times new roman",15), text='Name',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=0)
            # e.place(x=50,y=110)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Username',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=1)
            # e.place(x=150,y=110)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Contact',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=2)
            # e.place(x=250,y=110)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Email',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=3)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Question',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=4)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Answer',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=5)
            e=Label(Frame_table,width=11, font=("times new roman",15), text='Password',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=6)

            i=1
            for Login in cur:
                for j in range(len(Login)):
                    e = Label(Frame_table, width=11, font=("times new roman",15), text=Login[j],borderwidth=2,relief='ridge', anchor="w", bg="#5780B6")
                    e.grid(row=i, column=j)
                i=i+1
            
        except Exception as es:
            messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.root)


    def dashboard(self):
        root.destroy()
        import Worker_Dashboard

    def DeleteUser_Func(self):
        import Delete_Worker
    
    def Logout_Func(self):
        root.destroy()
        import login

    def AddUpdateUser_Func(self):
        root.destroy()
        import AddUpdateWorker
    
    def Back_Func(self):
        root.destroy()
        import Admin_Dashboard

root = Tk()
obj = page_User(root)
root.mainloop()
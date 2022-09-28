from tkinter import *
from tokenize import cookie_re
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class page_standrads:
    def __init__(self,root):
        self.root = root
        self.root.title("Standrads")
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
        Frame_standrad.place(x=1020, y=190, height=450, width=260)

        Frame_table = Frame(self.root, bg="#5780B6")
        Frame_table.place(x=580, y=190, height=450, widt=450)
    
        # -------------------------------------     Dashboard Area    -------------------------------
        
        add_btn = Button(Frame_standrad, text="Add Standards", command=self.Add_Standrads, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        add_btn.place(x=30, y=50, height=40, width=200)

        update_btn = Button(Frame_standrad, text="Update Standards", command=self.Add_Standrads, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        update_btn.place(x=30, y=150, height=40, width=200)

        delete_btn = Button(Frame_standrad, text="Delete Standards", command=self.Add_Standrads, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        delete_btn.place(x=30, y=250, height=40, width=200)

        
        # -------------------------------------    Table Generation   -------------------------------
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
            cur = con.cursor()
            cur.execute("SELECT * FROM standrads") 
            e=Label(Frame_table, width = 12, font=("times new roman",15,"bold"), text='id',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=0)
            # e.place(x=50,y=100)
            e=Label(Frame_table,width=12, font=("times new roman",15,"bold"), text='Lenght',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=1)
            # e.place(x=150,y=100)
            e=Label(Frame_table,width=12, font=("times new roman",15,"bold"), text='Width',borderwidth=2, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=2)
            # e.place(x=250,y=100)

            i=1
            for standrads in cur:
                for j in range(len(standrads)):
                    e = Label(Frame_table, width=12, font=("times new roman",15,"bold"), text=standrads[j],borderwidth=2,relief='ridge', anchor="w", bg="#5780B6")
                    e.grid(row=i, column=j)
                i=i+1
            
        except Exception as es:
            messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.root)


    def dashboard(self):
        root.destroy()
        import Worker_Dashboard
    
    def Logout_Func(self):
        root.destroy()
        import login

    def Add_Standrads(self):
        root.destroy()
        import addstandrads
    
    def Back_Func(self):
        root.destroy()
        import Worker_Dashboard 

root = Tk()
obj = page_standrads(root)
root.mainloop()
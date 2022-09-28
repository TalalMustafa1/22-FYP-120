from tkinter import *
from tokenize import cookie_re
from PIL import ImageTk
import PIL.Image
from tkinter import messagebox
import pymysql
import io

class page_Reports:
    def __init__(self,window):
        self.window = window
        self.window.title("Reports")
        self.window.geometry("1366x768")
        self.window.state("zoomed")

        # window icon 
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.window.iconphoto(True, win_icon)

        # =======================================================================================
        # ===========================  BACKGROUND IMAGE  ========================================
        # =======================================================================================

        self.back_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        backimage_label = Label(window, image=self.back_image)
        backimage_label.place(x=0, y=0 , width = 1366)
        # backimage_label.place(x=293, y=90, width=1073, height=750)

        # =======================================================================================
        # =================================  Header  ============================================
        # =======================================================================================

        title = Label(self.window, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28,"bold"), bg="#5780B6", fg="lightgray")
        title.place(x=0 , y=3, width=1366, height=90)
        back_btn = Button(self.window, text="Back", command=self.Back_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        back_btn.place(x=10, y=28)
        self.txt_logout = Button(self.window, text='Logout', command=self.Logout_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        self.txt_logout.place(x=1250, y=28)

        # --------------------------------------      Frame Set         ------------------------------------
        
        Frame_table = Frame(self.window, bg="#5780B6")
        Frame_table.place(x=820, y=200, height=500, width=550)
        # Frame_table.place(x=620, y=180, height=500, width=720)
        
        # -------------------------------------    Table Generation   -------------------------------
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
            cur = con.cursor()

            cur.execute("SELECT Pic_Id, Pic_Lenght, Pic_Width FROM reports") 
            e=Label(Frame_table, width = 20, font=("times new roman",15), text='ID',borderwidth=0, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=0)
            e=Label(Frame_table,width=20, font=("times new roman",15), text='Lenght',borderwidth=0, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=1)
            e=Label(Frame_table,width=20, font=("times new roman",15), text='Waist',borderwidth=0, relief='ridge',anchor='w',bg='#5780B6')
            e.grid(row=0,column=2)

            i=1
            for reports in cur:
                for j in range(len(reports)):
                    e = Label(Frame_table, width=20, font=("times new roman",15), text=reports[j],borderwidth=0,relief='ridge', anchor="w",bg="#5780B6")
                    e.grid(row=i, column=j)
                i=i+1
            
        except Exception as es:
            messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.window)
    
    def Logout_Func(self):
        window.destroy()
        import login
    
    def Back_Func(self):
        window.destroy()
        import Worker_Dashboard

window = Tk()
obj = page_Reports(window)
window.mainloop()
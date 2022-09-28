from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class add_standrads:
    def __init__(self,root):
        self.root = root
        self.root.title("Add / Update / Delete Standrads")
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

        # --------------  Login Form  ---------------------------
        Frame_login = Frame(self.root, bg="#5780B6")
        Frame_login.place(x=830, y=240, height=370, width=500)

        # Row 1
        title = Label(Frame_login, text="Add Here .....",font=("Impact",35,"bold"), fg="lightgray", bg="#5780B6").place(x=90, y=10)

        # Row 2
        id = Label(Frame_login, text="Standrad Id",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6").place(x=90, y=80)
        self.txt_id = Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_id.place(x=90, y=110, height=35, width=350)

        # Row 3
        lenght = Label(Frame_login, text="Standrad Lenght",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6").place(x=90, y=150)
        self.txt_lenght = Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_lenght.place(x=90, y=180, height=35, width=350)
        
        width = Label(Frame_login, text="Standrad Width",font=("Goudy old style",15,"bold"), fg="lightgray", bg="#5780B6").place(x=90, y=220)
        self.txt_width = Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_width.place(x=90, y=250, height=35, width=350)

    
        add_btn = Button(self.root, text="Add", command=self.add_data, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        add_btn.place(x=940, y=570, height=40, width=100)
        update_btn = Button(self.root, text="Update", command=self.update_data, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        update_btn.place(x=1050, y=570, height=40, width=100)
        delete_btn = Button(self.root, text="Delete", command=self.delete_data, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        delete_btn.place(x=1160, y=570, height=40, width=100)

    
    def Standrads(self):
        root.destroy()
        import standrads

    # def clear(self):
    #     self.txt_id.delete(0,END)
    #     self.txt_width.delete(0,END)
    #     self.txt_lenght.delete(0,END)
    
    def Back_Func(self):
        root.destroy()
        import standrads
    
    def Logout_Func(self):
        root.destroy()
        import login
        
    
    def update_data(self):
        if self.txt_id.get() == "" or self.txt_lenght.get() =="" or self.txt_width.get() == "":
            messagebox.showerror("Error", "All Feilds are Required", parent=self.root)
    
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("UPDATE standrads SET lenght= %s, width=%s WHERE id = %s",
                            (
                                
                                self.txt_lenght.get(),
                                self.txt_width.get(),
                                self.txt_id.get(),
                            )
                            )
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Updated Successfull", parent=self.root)
                self.Standrads()
                
                    
            except Exception as es:
                messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.root)



    def add_data(self):
        if self.txt_id.get() == "" or self.txt_lenght.get() =="" or self.txt_width.get() == "":
            messagebox.showerror("Error", "All Feilds are Required", parent=self.root)
    
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("select * from standrads where id=%s", self.txt_id.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Success", "Standrad Already Exist", parent=self.root)
                else:
                    cur.execute("insert into standrads (id, lenght, width) VALUES (%s,%s,%s)",
                                (
                                    self.txt_id.get(),
                                    self.txt_lenght.get(),
                                    self.txt_width.get(),
                                )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Added Successfull", parent=self.root)
                    self.Standrads()
                    # self.clear()
                    
            except Exception as es:
                messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.root)
    
    def delete_data(self):
        if self.txt_id.get() == "" or self.txt_lenght.get() =="" or self.txt_width.get() == "":
            messagebox.showerror("Error", "All Feilds are Required", parent=self.root)
    
        else:    
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
                cur = con.cursor()
                cur.execute("DELETE FROM standrads WHERE id=%s", self.txt_id.get())
                messagebox.showinfo("Success", "Deleted Successfull", parent=self.root)
                self.Standrads()
                # self.clear()
                con.commit()
                con.close()
                        
            except Exception as es:
                messagebox.showerror("Success", f"Error due to :  {str(es)}", parent=self.root)

root = Tk()
obj = add_standrads(root)
root.mainloop()
# =======================================================================================
# ===========================  INCLUDED LIBRARIES  ========================================
# =======================================================================================

from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from matplotlib.pyplot import title


# =======================================================================================
# ===========================  WINDOW DETAILS  ========================================
# =======================================================================================

class page_Worker:
    def __init__(self, window):
        self.window = window
        window.title('User Rights')
        self.window.geometry("1366x768")
        self.window.state('zoomed')

        # window icon 
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.window.iconphoto(True, win_icon)

        # =======================================================================================
        # ===========================  BACKGROUND IMAGE  ========================================
        # =======================================================================================

        self.back_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        backimage_label = Label(self.window, image=self.back_image)
        backimage_label.place(x=0, y=0 , width = 1366)
        # backimage_label.place(x=293, y=90, width=1073, height=750)

        # =======================================================================================
        # =================================  Header  ============================================
        # =======================================================================================

        title = Label(self.window, text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",28,"bold"), bg="#5780B6", fg="lightgray")
        title.place(x=0 , y=3, width=1366, height=90)
        self.txt_logout = Button(self.window, text='Logout', command=self.Logout_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2')
        self.txt_logout.place(x=1250, y=28)

        # =====================================================================================================
        # ============================================  BODY  =================================================
        # =====================================================================================================
        frame_worker = Frame(self.window, bg="#5780B6")
        frame_worker.place(x=840, y=240, width=480, height=480)

        title_frame = Label(frame_worker, text="Worker Functions",font=("Impact",28), fg="white", bg="#5780B6")
        title_frame.place(x=110, y=30)
        
        # =========================================  SCAN BUTTON  =============================================
        scan_btn = Button(frame_worker, text="Scan", command=self.scan, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white",font=("times new roman", 20))
        scan_btn.place(x=130, y=150, height=40, width=220)

        # ========================================  REPORT BUTTON  =============================================
        report_btn = Button(frame_worker, text="Report Details", command=self.Show_Report, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        report_btn.place(x=130, y=220, height=40, width=220)

        # =======================================  STANDRADS BUTTON  ============================================
        standrad_btn = Button(frame_worker, text="Standrads", command=self.Standrads_Func, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        standrad_btn.place(x=130, y=290, height=40, width=220)

    # =====================================================================================================
    # =====================================  BACKEND CODDING  =============================================
    # =====================================================================================================

    # ========================== Logout Function
    def Logout_Func(self):
        window.destroy()
        import login
    
    def Standrads_Func(self):
        window.destroy()
        import standrads

    # ========================== Scan FUNCTION
    
    def scan(self):
        window.destroy()
        import Scan_Image

    def Show_Report(self):
        window.destroy()
        import reports


window = Tk()
obj = page_Worker(window)
window.mainloop()

# =======================================================================================
# ===========================  INCLUDED LIBRARIES  ========================================
# =======================================================================================

from distutils.util import execute
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from matplotlib.pyplot import title
import pymysql
import cv2


# =======================================================================================
# ===========================  WINDOW DETAILS  ========================================
# =======================================================================================
# global w,h
class page_Scanning:
    def __init__(self, window):
        self.window = window
        window.title('Scanning')
        window.geometry("1366x768")
        window.state('zoomed')

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
        title.place(x=0 , y=0, width=1366, height=90)
        back_btn = Button(self.window, text="Back", command=self.back_func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        back_btn.place(x=10, y=28)
        self.txt_logout = Button(self.window, text='Logout', command=self.Logout_Func, bg='#5780B6', font=("Goudy", 16, "bold"),bd=0, fg='lightgray', cursor='hand2', activebackground='#32cf8e')
        self.txt_logout.place(x=1250, y=28)

        # =====================================================================================================
        # ============================================  BODY  =================================================
        # =====================================================================================================
        frame_worker = Frame(self.window, bg="#5780B6")
        frame_worker.place(x=840, y=240, width=480, height=480)

        title_frame = Label(frame_worker, text="Worker Functions",font=("Impact",28), fg="lightgray", bg="#5780B6")
        title_frame.place(x=110, y=30)
        
        # =========================================  SCAN BUTTON  =============================================
        scan_btn = Button(frame_worker, text="Scan", command=self.scan, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        scan_btn.place(x=130, y=150, height=40, width=220)

        # ========================================  REPORT BUTTON  =============================================
        report_btn = Button(frame_worker, text="Report Details", command=self.Show_Report, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 20))
        report_btn.place(x=130, y=220, height=40, width=220)

        message_frame = Label(frame_worker, text="Instuctions for Worker: While capturing image press \n 'S' for Save  and 'Q' for \n closing the camera ",font=("Arial",14), fg="cyan", bg="#5780B6")
        message_frame.place(x=20, y=320)


    # =====================================================================================================
    # =====================================  BACKEND CODDING  =============================================
    # =====================================================================================================

    # ========================== Logout Function
    def Logout_Func(self):
        window.destroy()
        import login
    
    def back_func(self):
        window.destroy()
        import Worker_Dashboard

    # ========================== Scan FUNCTION
    
    def scan(self):
     
        key = cv2.waitKey(1)
        webcam = cv2.VideoCapture(1)
        # webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
                cv2.imshow("Capturing Image", frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(filename='saved_img.jpg', img=frame)
                    webcam.release()
                    img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                    img_new = cv2.imshow("Captured Image", img_new)
                    cv2.waitKey(1650)
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Success","Image saved Successfully !!", parent = self.window)
                    print("Image saved!")
                    break
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break

            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                messagebox.showerror("Error","Camera not available",parent = window)
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
    
    def Show_Report(self):
       window.destroy()
       import reportdetails_win


window = Tk()
obj = page_Scanning(window)
window.mainloop()

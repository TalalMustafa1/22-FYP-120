# =======================================================================================
# ===========================  INCLUDED LIBRARIES  ========================================
# =======================================================================================

from distutils import extension
from distutils.util import execute
from this import d
from tkinter import *
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from matplotlib.pyplot import title
import pymysql
import cv2
import numpy as np
import matplotlib.image as image
from matplotlib import pyplot as plt

class page_Scanning():
    def __init__(self, window):
        global waist, length
        self.window = window
        window.title('Reports Details')
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
    # =====================================  BACKEND CODDING  =============================================
    # =====================================================================================================

    # =====================================================================================================
    # =====================================  IMAGE DETAILS  =============================================
    # =====================================================================================================
                # Load image, grayscale, Gaussian blur, Otsu's threshold, dilate

        # Import the image
        file_name = "saved_img.jpg"
        # file_name = "images/img1.jpeg"
        
        # Read the image
        src = cv2.imread(file_name, 1)
        
        # Convert image to image gray
        tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # Applying thresholding technique
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        
        # Using cv2.split() to split channels 
        # of coloured image
        b, g, r = cv2.split(src)
        
        # Making list of Red, Green, Blue
        # Channels and alpha
        rgba = [b, g, r, alpha]
        
        # Using cv2.merge() to merge rgba
        # into a coloured/multi-channeled image
        dst = cv2.merge(rgba, 4)
        
        # Writing and saving to a new image
        new_image=cv2.imwrite("images/gfg_white.png", dst)

        mask = cv2.imread('images/gfg_white.png') #The mask variable in your code
        # plt.imshow(mask)
        thresh_min,thresh_max = 127,255
        ret,thresh = cv2.threshold(mask,thresh_min,thresh_max,0)
        # findContours requires a monochrome image.
        thresh_bw = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
        # findContours will find contours on bright areas (i.e. white areas), hence we'll need to invert the image first
        thresh_bw_inv = cv2.bitwise_not(thresh_bw)

        contours, hierarchy = cv2.findContours(thresh_bw_inv,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # ^Gets all white contours

        # Find the index of the largest contour
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt=contours[max_index]

        x,y,w,h = cv2.boundingRect(cnt)
        waist_1 = (w*0.0264583333)*3-12
        length_1 = (h*0.0264583333)*5-10

        print (waist_1)
        print (length_1) 

        Remarks = []
        if (waist_1 == 37 and length_1 == 40):
            # print("Remarks is approved")
            Remarks = "Accepted"
        else:
            # print("Remarks is not approved")
            Remarks = "Rejected"

        # Remarks = ""
        # Approved = ""
        # Not_Approved = ""
        # if (waist_1 == 36 and length_1 == 42):
        #     return Approved
        # else:
        #     print("Remarks is not approved")
        #     return Not_Approved

        original_label = Label(self.window, text="Origional Image",font=("Arial",22),fg='lightgray',bg='#5780B6')
        original_label.place(x=110, y=100)
        # Frame for Original Image
        frame_img1 = Frame(self.window, bg="white")
        frame_img1.place(x=6, y=145, width=500, height=555)
        # Create an object of tkinter ImageTk
        # img = Image.open("images/img1.jpeg")
        img = Image.open("saved_img.jpg")
        img= img.resize((500,555))
        self.img=ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        self.label = Label(frame_img1, image = self.img)
        self.label.pack()

        roi_label = Label(self.window, text="Region of Interest",font=("Arial",22),fg='lightgray',bg='#5780B6')
        roi_label.place(x=640, y=100)    
        # Frame for ROI image
        frame_img2 = Frame(self.window, bg="white")
        frame_img2.place(x=510, y=145, width=500, height=555)

        # Create an object of tkinter ImageTk
        img2 = Image.open("images/gfg_white.png")
        img2= img2.resize((500,555))
        self.img3=ImageTk.PhotoImage(img2)
        # Create a Label Widget to display the text or Image
        self.label1 = Label(frame_img2, image = self.img3)
        self.label1.pack()

        details_label = Label(self.window, text="Garment Dimensions",font=("Arial",22),fg='lightgray',bg='#5780B6')
        details_label.place(x=1060, y=100)
        
        details_frame = Frame(self.window,bg='#5780B6')
        details_frame.place(x=1015, y=145, width=345, height=555)

        width_label = Label(details_frame, text="Width of Pant: %d inch"  %(waist_1),font=("Arial",22),fg='lightgray',bg='#5780B6')
        width_label.place(x=50, y=120)

        details_label = Label(details_frame, text="Length of Pant: %d inch" %(length_1) ,font=("Arial",22),fg='lightgray',bg='#5780B6')
        details_label.place(x=50, y=190)

        details_dat = Label(details_frame, text="Remarks = " +Remarks, font=("Arial",22),fg='lightgray',bg='#5780B6')
        details_dat.place(x=50, y=260)

        global filelocation
        filelocation = "images/gfg_white.png"
        file = open(filelocation,"rb")
        file = file.read()

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="mfd_system")
            cur = con.cursor()
            sql = "insert into reports (Pic_Lenght,Pic_Width,Picture) values (%s, %s, %s)"
            Val = [(length_1, waist_1, file)]
            cur.executemany(sql,Val)
            con.commit()
            con.close()
            # messagebox.showinfo("Success", "Image Inserted Successfull", parent=self.window)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to :  {str(es)}", parent=self.window)

       # ========================== Logout Function

    def Logout_Func(self):
        window.destroy()
        import login
    
    def back_func(self):
        window.destroy()
        import Scan_Image

window = Tk()
obj = page_Scanning(window)
window.mainloop()

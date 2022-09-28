from tkinter import *
from PIL import Image , ImageTk
class page_main:
    def __init__ (self,window):
        self.window = window
        self.window.title("Garment Measurement & Fault Detection System")
        self.window.geometry("1366x768")
        self.window.state("zoomed")

        # window icon 
        win_icon = ImageTk.PhotoImage(file = 'images/window_icon.ico')
        self.window.iconphoto(True, win_icon)

        # Background Image 
        self.back_image = ImageTk.PhotoImage(file = 'images/backgound.jpg')
        backimage_label = Label(self.window, image=self.back_image)
        backimage_label.place(x=0, y=0 , width = 1366)
        # backimage_label.place(x=293, y=90, width=1073, height=750)

        # Label of MFDS
        title = Label( text="GARMENT MEASUREMENT & FAULT DETECTION SYSTEM",font=("times new roman",30,"bold"), bg="#5780B6", fg="lightgray")
        # title.place(x=110, y=20)
        title.place(x=0 , y=0, width=1366, height=90)

        # Let's Started Button
        next_btn = Button(self.window, text="Get Started..", command=self.LoginPage, fg="black", bg="lightgray", activebackground="#5780B6",activeforeground="white", font=("times new roman", 26, "bold"))
        next_btn.place(x=1010, y=590, width= 250, height=60)
    
    def LoginPage(self):
        window.destroy()
        import login
window = Tk()
obj = page_main(window)
window.mainloop()
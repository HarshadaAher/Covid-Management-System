from tkinter import *
from add import addpatient
from tracker import Tracker
from time import sleep
from world_tracker import Info
from PIL import ImageTk,Image


def baseed():
    root.destroy()
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("  COVID-19 MANAGEMENT SYSREM       ")
        self.root.geometry("1230x650+30+15")
        self.root.config(bg="white")
        self.root.resizable(False, False)


        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\img1.png"))
        self.lable = Label(self.root, image=self.image)
        self.lable.pack()



        self.root.config(bg="white")
        self.logo=ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\hed_log.png"))

        title = Label(self.root, text="Covid-19 ",font=("Algerian", 50, "bold"),bg="#6fa8dc",
                 fg="black").place(x=0, y=0,relwidth=1,  height=65)
        itle = Label(self.root, text="Management System", font=("Aharoni", 34, "bold"), bg="#6fa8dc",
                     fg="#073763").place(x=0, y=65, relwidth=1, height=55)
        self.image1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\2.png"))
        self.lable = Label(self.root, image=self.image1)
        self.lable.place(x=0, y=0)
        self.image2 = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\fli.png"))
        self.lable = Label(self.root, image=self.image2)
        self.lable.place(x=980, y=0)



        #==buttons==
        bt_add_patient=Button(text="Add New Patient",font=("goudy old style",15,"bold"),bg="#6fa8dc",fg="black",cursor="hand2",bd=5,command=self.add_patient).place(x=200,y=560,width=200,height=50)
        bt_tracker=Button(text="Covid Patients-2020",font=("goudy old style",15,"bold"),bg="#6fa8dc",fg="black",cursor="hand2",bd=5,command=self.show_tracker).place(x=700,y=560,width=200,height=50)
        bt_moreinfo=Button(text="More-Info",font=("goudy old style",15,"bold"),bg="#6fa8dc",fg="black",cursor="hand2",bd=5,command=self.show_info).place(x=450,y=560,width=210,height=50)

        bt4=Button(text="Exit",font=("goudy old style",15,"bold"),bg="#6fa8dc",fg="black",cursor="hand2",bd=5,command=baseed).place(x=955,y=560,width=110,height=50)


    def add_patient(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=addpatient(self.new_window)

    def show_tracker(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=Tracker(self.new_window)

    def show_info(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=Info(self.new_window)


if __name__=="__main__":
    root= Tk()
    obj=RMS(root)
    root.mainloop()

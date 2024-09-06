from tkinter import *
from PIL import  Image,ImageTk
from tkinter import ttk,messagebox
from twilio.rest import Client
import sqlite3
class Report:

    def __init__(self,root):

        self.root=root
        self.root.title("Report")
        self.root.geometry("1230x550+30+15")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        self.root.focus_force()

        #==TitleC:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\Screenshot(149).png

        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\Screenshot (149).png"))
        self.lable = Label(self.root, image=self.image)
        self.lable.pack()
        title = Label(self.root, text="Send Report ",font=("goudy old style", 20, "bold"), bg="orange",
                      fg="black").place(x=0, y=0, width=1300, height=40)
        self.image2 = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\1.png"))
        self.lable = Label(self.root, image=self.image2)
        self.lable.place(x=900, y=380)


        #=========serch
        self.var_ser=StringVar()
        self.var_no=StringVar()

        serch_lb=Label(self.root,text="Search by Name",font=("goudy old style", 18, "bold"),bg="white").place(x=120,y=100)
        txt_serch_lb=Entry(self.root,textvariable=self.var_ser,font=("goudy old style", 18),bg="lightyellow",width=29).place(x=320,y=100)

        btn_serch = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="black",
                           cursor="hand2",command=self.search)
        btn_serch.place(x=701, y=100, width="80", height="37")

        btn1_clear = Button(self.root, text="clear", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="black",
                           cursor="hand2",command=self.clear)
        btn1_clear.place(x=801, y=100, width="80", height="37")

        #=========================lable

        lb_id=Label(self.root,text="ID",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=100,y=230,width=90,height=25)
        lb_name=Label(self.root,text="Name",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=185,y=230,width=130,height=25)
        lb_dr=Label(self.root,text="Doctor",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=130,height=25)
        lb_ho=Label(self.root,text="Hospital",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=420,y=230,width=120,height=25)
        lb_gen=Label(self.root,text="Gender",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=520,y=230,width=110,height=25)
        lb_mb=Label(self.root,text="Mobile",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=630,y=230,width=140,height=25)
        lb_sw=Label(self.root,text="Swab No",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=760,y=230,width=100,height=25)
        lb_sd=Label(self.root,text="Sample Date",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=860,y=230,width=150,height=25)
        lb_re=Label(self.root,text="Report",font=("goudy old style", 15, "bold"),bg="white",bd=2,relief=GROOVE).place(x=1000,y=230,width=100,height=25)

        self.id = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.id.place(x=100, y=255, width=130, height=30)

        self.name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2,
                        relief=GROOVE)
        self.name.place(x=185, y=255, width=120, height=30)

        self.dr = Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.dr.place(x=300, y=255, width=120, height=30)

        self.ho = Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.ho.place(x=420, y=255, width=100, height=30)

        self.gen = Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.gen.place(x=520, y=255, width=130, height=30)
        self.mb = Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.mb.place(x=630, y=255, width=130, height=30)
        self.sw= Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.sw.place(x=760, y=255, width=100, height=30)
        self.sd= Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.sd.place(x=860, y=255, width=150, height=30)
        self.re= Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2,
                      relief=GROOVE)
        self.re.place(x=1000, y=255, width=100, height=30)

        btn1_delete = Button(self.root, text="Send report via SMS", font=("goudy old style", 15, "bold"), bg="red", fg="black",
                            cursor="hand2",command=self.send)
        btn1_delete.place(x=450, y=400, width="260", height="47")
        btn1_exit = Button(self.root, text="Exit", font=("goudy old style", 15, "bold"), bg="lightyellow",
                             fg="black",bd=5,cursor="hand2", command=self.exi)
        btn1_exit.place(x=520, y=490, width="90", height="47")
#==========================
    def search(self):

        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            if self.var_ser.get()=="":
                messagebox.showerror("Error","Name should be required",parent=self.root)
            else:
                 cur.execute("select * from patient where name=?",( self.var_ser.get(),))
                 row = cur.fetchone()
                 if row!=None:
                    self.id.config(text=row[0])
                    self.name.config(text=row[1])
                    self.dr.config(text=row[2])
                    self.ho.config(text=row[3])
                    self.gen.config(text=row[4])
                    self.mb.config(text=row[5])
                    self.sw.config(text=row[6])
                    self.sd.config(text=row[7])
                    self.re.config(text=row[8])

                 else:
                     messagebox.showerror("Error","No such record found",parent=self.root)
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to {str(ex)}")


#==============================================================================

    def send(self):
        client = Client("ACf64f32e7ee718e048110fb72f858f8d1", "79e5851bf89d408685957b872b38d799")
        client.messages.create(to=["+91 9970795983"],
                               from_="+13853931535",
                               body="SAYALI GAROLE (Swab no.: CoV2699) (25/03/2021)Your RT-PCR is NEGATIVE By VRDL GMCH A'bad'.This message is computer gernarated .No need for signature. ")
        messagebox.showinfo("Success", "Report Sent Successfully.!")







#======================================================================
    def clear(self):
        self.id.config(text="")
        self.name.config(text="")
        self.dr.config(text="")
        self.ho.config(text="")
        self.gen.config(text="")
        self.mb.config(text="")
        self.sw.config(text="")
        self.sd.config(text="")
        self.re.config(text="")
        self.var_ser.set("")

    def exi(self):
        self.root.destroy()


if __name__=="__main__":
    root= Tk()
    o=Report(root)
    root.mainloop()
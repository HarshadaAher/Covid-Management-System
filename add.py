from tkinter import *
from PIL import  Image,ImageTk
from tkinter import ttk,messagebox
from report import Report
import sqlite3

class addpatient:

    def __init__(self,root):

        self.root=root
        self.root.title("    Add Patient Details ")
        self.root.geometry("1230x550+30+15")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.focus_force()

        #==Title

        self.image = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\bg2.png"))
        self.lable = Label(self.root, image=self.image)
        self.lable.pack()

        title = Label(self.root, text="Patient Details",font=("Algerian", 30, "bold"), bg="#b6d7a8",
                      fg="black").place(x=0, y=0, relwidth=1, height=45)
        self.image1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Sayali\\Desktop\\covid\\covid_pro\\hed_log.png"))
        self.lable = Label(self.root, image=self.image1)
        self.lable.place(x=1090, y=0)



        #=========variable================

        self.var_id=StringVar()
        self.var_nm=StringVar()
        self.var_dr=StringVar()
        self.var_hospital=StringVar()
        self.var_gender=StringVar()
        self.var_mb_no=StringVar()
        self.var_swap_no=StringVar()
        self.var_swap_date=StringVar()
        self.var_report=StringVar()

        #============widgets=====

        lb2_patient_nm=Label(self.root,text="Patient name",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=90)
        lb3_doctor_nm=Label(self.root,text="Doctor name",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=140)
        lb4_Hospital_nm=Label(self.root,text="Hospital name",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=190)
        lb5_gender=Label(self.root,text=" Gender",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=240)
        lb6_mobile_no=Label(self.root,text="Mobile no",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=290)
        lb7_swap_no=Label(self.root,text="Swab Number",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=340)
        lb8_sample_date=Label(self.root,text="Date of Sample Taken",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=390)
        lb9_report=Label(self.root,text="Report",font=("goudy old style", 15, "bold"),bg="white").place(x=10,y=440)

        #==========textEntry=========

        self.txt_patient_nm = Entry(self.root, textvariable=self.var_nm, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_patient_nm.place(x=210, y=90,width=300)
        self.txt_doctor_nm = Entry(self.root, textvariable=self.var_dr,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_doctor_nm.place(x=210, y=140,width=300)
        self.txt_Hospital_nm = Entry(self.root,  textvariable=self.var_hospital,font=("goudy old style", 15, "bold"),
                                bg="lightyellow")
        self.txt_Hospital_nm.place(x=210, y=190,width=300)
        self.txt_gender = ttk.Combobox(self.root,  textvariable=self.var_gender,values=("Select","Male","Female"),font=("goudy old style", 15, "bold"), state="readeonly",justify=CENTER)
        self.txt_gender .place(x=210,y=240,width=300)
        self.txt_gender.current(0)
        self.txt_mobile_no = Entry(self.root,textvariable=self.var_mb_no,  font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_mobile_no.place(x=210,y=290,width=300)
        self.txt_swap_no = Entry(self.root, textvariable=self.var_swap_no, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_swap_no.place(x=210,y=340,width=300)
        self.txt_sample_date = Entry(self.root, textvariable=self.var_swap_date,font=("goudy old style", 15, "bold"),
                                bg="lightyellow")
        self.txt_sample_date.place(x=210, y=390,width=300)
        self.txt_report = ttk.Combobox(self.root,textvariable=self.var_report ,values=("Select","Positive","Negative"), font=("goudy old style", 15, "bold"), state="readeonly",justify=CENTER)
        self.txt_report .place(x=210, y=440,width=300)
        self.txt_report.current(0)


        #Button========================

        self.btn_add=Button(self.root,text="Add",font=("goudy old style", 15, "bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.addd)
        self.btn_add.place(x=50,y=500,width="120",height="40")
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=500, y=500, width=110, height="40")
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                              cursor="hand2",command=self.update)
        self.btn_update.place(x=200, y=500, width="110", height="40")
        self.btn_clear = Button(self.root, text="clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                            cursor="hand2",command=self.clear)
        self.btn_clear.place(x=350, y=500, width="110", height="40")
        self.btn_send_re = Button(self.root, text="Send Report", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                                cursor="hand2",command=self.send_rep)
        self.btn_send_re.place(x=650, y=500, width="140", height="40")
        self.btn1e_send_re = Button(self.root, text="Exit", font=("goudy old style", 15, "bold"), bg="#607d8b",
                                  fg="white",bd=3,
                                  cursor="hand2", command=self.end)
        self.btn1e_send_re.place(x=850, y=500, width="100", height="40")




#==========Search pannel+===========

        self.serch_var=StringVar()
        lb_serch_patient_nm=Label(self.root,text="name:",font=("goudy old style",16,"bold"),bg="white").place(x=600,y=80)
        search_patient= Entry(self.root, textvariable=self.serch_var, font=("goudy old style", 15, "bold"), bg= "lightyellow")
        search_patient.place(x=690, y=80, width=279,height="35")
        btn_serch = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="black",
                              cursor="hand2",command=self.search)
        btn_serch.place(x=990, y=80, width="80", height="35")

        #===========contetbox===========
        self.c_frame=Frame(self.root,bd=2,bg="black",relief=RIDGE)
        self.c_frame.place(x=590,y=110,height=390)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.content_table=ttk.Treeview(self.c_frame,columns=("pid","name","Doctor","Hospital","Gender","Contact","Swap_NO","Date","Report"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.config(command=self.content_table.yview)
        scrollx.config(command=self.content_table.xview)
        self.c_frame.place(x=579,y=130,height=350,width=610)
        self.content_table.heading("pid",text="ID")
        self.content_table.heading("name",text="Name")
        self.content_table.heading("Doctor",text="Doctor")
        self.content_table.heading("Hospital",text="Hospital")
        self.content_table.heading("Gender",text="Gender")
        self.content_table.heading("Contact",text="Contact")
        self.content_table.heading("Swap_NO",text="Swap")
        self.content_table.heading("Date",text="Date")
        self.content_table.heading("Report",text="Report")
        self.content_table["show"]="headings"
        self.content_table.column("pid", width=90)
        self.content_table.column("name", width=90)
        self.content_table.column("Doctor", width=90)
        self.content_table.column("Hospital", width=90)
        self.content_table.column("Gender", width=90)
        self.content_table.column("Contact", width=90)
        self.content_table.column("Swap_NO", width=90)
        self.content_table.column("Date", width=90)
        self.content_table.column("Report", width=90)
        self.content_table.pack(fill=BOTH,expand=1)
        self.content_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()

# ================================================================================================
    def delete(self):
        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            if self.var_nm.get()=="":
                messagebox.showerror("Error","Patient Name is Required ",parent=self.root)
            else:
                cur.execute("select * from patient where name=?",( self.var_nm.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerrorcur("Please Select the patient from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete? ",parent=self.root)
                    if op==True:
                        cur.execute("delete from patient where name=?",(self.var_nm.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Patient details Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#================================================================================================

    def clear(self):
        self.show()
        self.var_nm.set("")
        self.var_dr.set("")
        self.var_hospital.set("")
        self.var_gender.set("")
        self.var_mb_no.set("")
        self.var_swap_no.set("")
        self.var_swap_date.set("")
        self.var_report.set("")
        self.serch_var.set("")
        self.txt_patient_nm.config(state=NORMAL)

#================================================================================================

    def get_data(self,ev):
        self.txt_patient_nm.config(state="readonly")
        self.txt_patient_nm
        r=self.content_table.focus()
        content=self.content_table.item(r)
        row=content["values"]
        #print Rows
        self.var_nm.set(row[1])
        self.var_dr.set(row[2])
        self.var_hospital.set(row[3])
        self.var_gender.set(row[4])
        self.var_mb_no.set(row[5])
        self.var_swap_no.set(row[6])
        self.var_swap_date.set(row[7])
        self.var_report.set(row[8])
#===========================================================================
    def addd(self):
        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            if self.var_nm.get()=="":
                messagebox.showerror("Error","Patient Name is Required ",parent=self.root)
            else:
                cur.execute("select * from patient where name=?",( self.var_nm.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerrorcur("Error","Patient Name Alredy Present",parent=self.root)
                else:
                    cur.execute("insert into patient (name,Doctor,Hospital,Gender,Contact,Swap_NO,Date,Report)values(?,?,?,?,?,?,?,?)",(
                            self.var_nm.get(),
                            self.var_dr.get(),
                            self.var_hospital.get(),
                            self.var_gender.get(),
                            self.var_mb_no.get(),
                            self.var_swap_no.get(),
                            self.var_swap_date.get(),
                            self.var_report.get()
                ))
                con.commit()
                messagebox.showinfo("Success","Patient added Successfully.",parent=self.root)
                self.show()
                self.clear()
                self.txt_patient_nm.focus()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#===========================================================================

    def update(self):
        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            if self.var_nm.get()=="":
                messagebox.showerror("Error","Patient Name is Required ",parent=self.root)
            else:
                cur.execute("select * from patient where name=?",( self.var_nm.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerrorcur("Error","Select patient from list",parent=self.root)
                else:
                    cur.execute("update patient set Doctor=?,Hospital=?,Gender=?,Contact=?,Swap_NO=?,Date=?,Report=? where name=?",(
                            self.var_dr.get(),
                            self.var_hospital.get(),
                            self.var_gender.get(),
                            self.var_mb_no.get(),
                            self.var_swap_no.get(),
                            self.var_swap_date.get(),
                            self.var_report.get(),
                            self.var_nm.get()
                    ))
                con.commit()
                messagebox.showinfo("Success","Patient updated Successfully.",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Errorn due to {str(ex)}")

 # ===========================================================================

    def show(self):
        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            cur.execute("select * from patient")
            rows=cur.fetchall()
            self.content_table.delete(*self.content_table.get_children())
            for row in rows:
                  self.content_table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

 # ===========================================================================

    def search(self):
        con = sqlite3.connect(database="covid_db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from patient  where name LIKE '%{self.serch_var.get()}%' ")
            rows=cur.fetchall()
            self.content_table.delete(*self.content_table.get_children())
            for row in rows:
                  self.content_table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Errorn due to {str(ex)}")

    def send_rep(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=Report(self.new_window)

    def end(self):
        self.root.destroy()

if __name__=="__main__":
    root= Tk()
    obj=addpatient(root)
    root.mainloop()


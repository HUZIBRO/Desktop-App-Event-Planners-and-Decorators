import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import fun5
from fun5 import *

def hr1():
    r1=tk.Tk()
    r1.attributes('-fullscreen',True)
    r1.title('Hall Record')

    Label(r1, text='S.H.M PLANNER\'S AND DECORATOR\'S  \n\nHall Records', font='times 21 bold').pack(side=TOP)

    Label(r1, text='##########################################################################################'
                     '##########################################################################################'
                     '##########################################################################################').place(x=5, y=150)

    Label(r1,text='Enter Contact Number or Order id',font='times 18 bold').place(x=50,y=200)
    sea=Entry(r1,bd=5)
    sea.place(x=450,y=200,height=30,width=200)



    Label(r1,text='Status ',font='times 18 bold').place(x=50,y=300)
    st=ttk.Combobox(r1)
    st['values']=['paid','Un-Paid']
    st.place(x=150,y=300,height=30,width=200)


    l1=Label(r1, text='Name ', font='times 15 bold ').place(x=50, y=400)
    l2=Label(r1, text='Contact ', font='times 15 bold ').place(x=50, y=460)
    l3=Label(r1, text='Venue ', font='times 15 bold ').place(x=50, y=520)
    l4=Label(r1, text='Date ', font='times 15 bold ').place(x=50, y=580)
    l5=Label(r1, text='Price ', font='times 15 bold ').place(x=50, y=640)


    e1 = Entry(r1, bd=4)
    e1.place(x=200, y=400, height=30, width=200)

    e2 = Entry(r1, bd=4)
    e2.place(x=200, y=460, height=30, width=200)

    e3 = Entry(r1, bd=4)
    e3.place(x=200, y=520, height=30, width=200)

    e4 = Entry(r1, bd=4)
    e4.place(x=200, y=580, height=30, width=200)

    e5 = Entry(r1, bd=4)
    e5.place(x=200, y=640, height=30, width=200)




    def alldata():
        if c_h(sea.get()) == True:
            if len(sea.get()) == 11:
                curs.execute(f"select * from Hall_main where contact = {int(sea.get())}")
                da=curs.fetchall()
                l=[]
                for val in da:
                    l.append(int(val[0]))
                    l.append(val[1])
                    l.append(int(val[2]))
                    l.append(val[3])
                    l.append(int(val[4]))
                    l.append(val[5])
                    l.append(val[6])
                e1.insert('end',l[1])
                e2.insert('end', l[2])
                e3.insert('end', l[3])
                e4.insert('end', l[5])
                e5.insert('end', l[4])

                st.insert('end',l[6])

            if len(sea.get()) != 11:
                curs.execute(f"select * from Hall_main where orderid = {int(sea.get())}")
                da = curs.fetchall()
                l = []
                for val in da:
                    l.append(int(val[0]))
                    l.append(val[1])
                    l.append(int(val[2]))
                    l.append(val[3])
                    l.append(int(val[4]))
                    l.append(val[5])
                    l.append(val[6])
                e1.insert('end', l[1])
                e2.insert('end', l[2])
                e3.insert('end', l[3])
                e4.insert('end', l[5])
                e5.insert('end', l[4])

                st.insert('end', l[6])
            elif len(sea.get()) <=0:
                messagebox.showerror('Error','Enter Valid Value')
        else:
            messagebox.showerror("Error","Not Exist")


    Button(r1, text='search',command=alldata, font='times 16 bold', padx=45, pady=0, bd=4).place(x=700, y=195)
    Label(r1,text='=========================================================================================='
                    '=========================================================================================='
                    '==========================================================================================').place(x=5,y=350)
    Label(r1, text='=========================================================================================='
                     '=========================================================================================='
                     '==========================================================================================').place(x=5, y=800)
    def r():
        m=messagebox.askquestion('Confirm ','Remove ?')
        if m== 'yes':
            if len(sea.get()) == 11:
                curs.execute(f"delete from Hall_main where contact = {int(sea.get())} ")
                curs.commit()
            if len(sea.get()) != 11:
                curs.execute(f"delete from Hall_main where orderid = {int(sea.get())} ")
                curs.commit()
            messagebox.showinfo("Removed",'Record Removed')
        else:
            messagebox.showinfo('Confirmation','Okay !')
    def u():
        a=messagebox.askyesno('Confirm ',"Are You Sure ?")
        if len(sea.get()) == 11:
            if a != 'No':
                s=f"{st.get()}"
                curs.execute(f"update Hall_main set status = '{s}' where contact = {sea.get()} ")
                curs.commit()
                messagebox.showinfo('Done',"Updated")
            else:
                messagebox.showinfo('Cancelled','Okay')
        if len(sea.get()) != 11:
            if a != 'No':
                s=f"{st.get()}"
                curs.execute(f"update Hall_main set status = '{s}' where orderid ={sea.get()} ")
                curs.commit()
                messagebox.showinfo('Done',"Updated")
            else:
                messagebox.showinfo('Cancelled','Okay')

    Button(r1, text='Remove',command=r, font='times 16 bold', padx=45, pady=0, bd=6).place(x=480, y=830)
    Button(r1, text='Update',command=u, font='times 16 bold', padx=45, pady=0, bd=6).place(x=900, y=830)
    Button(r1,text="Exit",command=r1.destroy,font='times 16 bold',padx=45,pady=0,bd=6).place(x=700,y=830)

    r1.mainloop()


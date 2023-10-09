import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
import fun5
from fun5 import *

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-UVB1NIM;"
            "Database=CAT;"
            "Trusted_Connection=yes;")

cur= pyodbc.connect(cnxn_str)

curs=cur.cursor()

def hr():
    root=tk.Tk()
    root.attributes('-fullscreen',True)
    root.title('Hall Record')

    Label(root, text='S.H.M PLANNER\'S AND DECORATOR\'S  \n\nDecoration Records', font='times 21 bold').pack(side=TOP)

    Label(root, text='##########################################################################################'
                     '##########################################################################################'
                     '##########################################################################################').place(x=5, y=150)

    Label(root,text='Enter Contact Number or Order id',font='times 18 bold').place(x=50,y=200)
    en=Entry(root,bd=5)
    en.place(x=450,y=200,height=30,width=200)

    l1=Label(root, text='Name ', font='times 17 bold ').place(x=50, y=300)
    l2=Label(root, text='Contact ', font='times 17 bold ').place(x=50, y=360)
    l3=Label(root, text='Venue ', font='times 17 bold ').place(x=50, y=420)
    l4=Label(root, text='Decoration ', font='times 17 bold ').place(x=50, y=480)
    l5=Label(root, text='Date ', font='times 17 bold ').place(x=50, y=540)
    l6=Label(root, text='Price ', font='times 17 bold ').place(x=50, y=600)
    l7=Label(root, text='Address ', font='times 17 bold ').place(x=50, y=660)

    e1 = Entry(root, bd=4)
    e1.place(x=200, y=300, height=30, width=200)

    e2 = Entry(root, bd=4)
    e2.place(x=200, y=360, height=30, width=200)

    e3 = Entry(root, bd=4)
    e3.place(x=200, y=420, height=30, width=200)

    e4 = Entry(root, bd=4)
    e4.place(x=200, y=480, height=30, width=200)

    e5 = Entry(root, bd=4)
    e5.place(x=200, y=540, height=30, width=200)

    e6 = Entry(root, bd=4)
    e6.place(x=200, y=600, height=30, width=200)

    e7 = Entry(root, bd=4)
    e7.place(x=200, y=660, height=30, width=200)



    Label(root,text='=========================================================================================='
                    '=========================================================================================='
                    '==========================================================================================').place(x=5,y=250)
    Label(root, text='=========================================================================================='
                     '=========================================================================================='
                     '==========================================================================================').place(x=5, y=800)
    def c_dec(inp):
        if len(inp) == 11:
            curs.execute(f"select contact from dec_c where contact = {int(inp)}")
            d = curs.fetchall()
            l = []
            for val in d:
                l.append(int(val[0]))
            if int(inp) in l:
                return True
            else:
                return False
    def r_dec():
        if len(en.get()) > 0:
            if c_d(en.get()) == True:
                if len(en.get()) == 11:
                    curs.execute(f"delete from decoration where contact = {int(en.get())} ")
                    curs.commit()
                    messagebox.showinfo('Removal','Removed Record ')
                else:
                    curs.execute(f"delete from decoration where orderid = {int(en.get())} ")
                    curs.commit()
            elif c_d(en.get()) == False:
                curs.execute(f"delete from dec_c where contact = {int(en.get())} ")
                curs.commit()
                messagebox.showinfo('Removal', 'Removed Record ')
            else:
                messagebox.showinfo('Error', 'No Record ')
        else:
            messagebox.showerror('Error','Enter a value')


    def dec():
        if len(en.get()) > 0:
            if c_d(en.get()) == False and c_dec(en.get()) == True:
                if len(en.get()) == 11:
                    curs.execute(f"select * from dec_c where contact = {int(en.get())}")
                    d = curs.fetchall()
                    l = []
                    for val in d:
                        for x in range(0, 7):
                            l.append(val[x])

                    n=l[0]
                    c=l[1]
                    v=l[2]
                    dec=l[3]
                    da=l[4]
                    p=l[5]
                    a=l[6]

                    e1.insert('end',n)
                    e2.insert('end', c)
                    e3.insert('end', v)
                    e4.insert('end', dec)
                    e5.insert('end', da)
                    e6.insert('end', p)
                    e7.insert('end', a)

            elif c_d(en.get()) == True:
                if len(en.get()) == 11:
                    curs.execute(f"select * from decoration where contact = {int(en.get())}")
                    d = curs.fetchall()
                    l = []
                    for val in d:
                        for x in range(0, 7):
                            l.append(val[x])

                    n=l[1]
                    c=l[2]
                    v=l[3]
                    dec=l[6]
                    da=l[5]
                    p=l[4]


                    e1.insert('end',n)
                    e2.insert('end', c)
                    e3.insert('end', v)
                    e4.insert('end', dec)
                    e5.insert('end', da)
                    e6.insert('end',p)





                if len(en.get()) < 11:
                    curs.execute(f"select * from decoration where orderid = {int(en.get())}")
                    d = curs.fetchall()
                    l = []
                    for val in d:
                        for x in range(0, 7):
                            l.append(val[x])

                    n = l[1]
                    c = l[2]
                    v = l[3]
                    dec = l[6]
                    da = l[5]

                    e1.insert('end', n)
                    e2.insert('end', c)
                    e3.insert('end', v)
                    e4.insert('end', dec)
                    e5.insert('end', da)
                    e6.insert('end', p)
            else:
                messagebox.showerror('Error',"Value don't exist ")
        else:
            messagebox.showerror('Error', "Enter A Value ")

    Button(root, text='Search',command=dec, font='times 16 bold', padx=45, pady=0, bd=6).place(x=700, y=195)
    Button(root,text="Exit",command=root.destroy,font='times 16 bold',padx=45,pady=0,bd=6).place(x=600,y=830)
    Button(root,text="Remove",command=r_dec,font='times 16 bold',padx=45,pady=0,bd=6).place(x=800,y=830)

    root.mainloop()


import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-UVB1NIM;"
            "Database=CAT;"
            "Trusted_Connection=yes;")

cur= pyodbc.connect(cnxn_str)

curs=cur.cursor()


def add_hall(o,n,c,v,p,d,s):
    curs.execute(f"insert into Hall_main(orderid,name,contact,venue,price,date,status) VALUES({o},'{n}',{c},'{v}',{p},'{d}','{s}')")
    curs.commit()

def hall():
    lis=[]
    b_number1=random.randrange(1,1000000)
    b_number=0
    if b_number1 not in lis:
        lis.append(b_number1)
        b_number=b_number1
    elif b_number1 in lis:
        b_number=b_number1


    root=tk.Tk()
    root.title('Hall Booking')
    root.attributes('-fullscreen',True)

    f=Frame(root,bd=5)
    f.place(x=565,y=330,height=460,width=1030)

    Label(root,text='S.H.M PLANNER\'S AND DECORATOR\'S  \n\nHALL BOOKING',font='times 21 bold').pack(side=TOP)
    Label(root, text=' ').pack(side=BOTTOM)
    Button(root,text='Exit',command=root.destroy,font='times 16 bold',bg='light grey',padx=45,pady=0).place(x=680,y=830)


    Button(root,text="Place Order",font='times 16 bold',bg='light grey',padx=45,pady=0).place(x=300,y=830)

    Button(root, text="Decorations's", font='times 16 bold', bg='light grey', padx=45, pady=0).place(x=950, y=830)

    Label(root,text='Name ',font='times 22 bold ').place(x=120,y=200)
    e1=Entry(root,bd=5)
    e1.place(x=205,y=205,height=30,width=200)

    Label(root, text='Contact Number  ', font='times 22 bold ').place(x=460, y=200)
    e2=Entry(root, bd=5)
    e2.place(x=680, y=205,height=30,width=200)

    Label(root, text='Email', font='times 22 bold ').place(x=1020, y=200)
    em=Entry(root, bd=5)
    em.place(x=1120, y=205,height=30,width=200)

    Label(root,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                    "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=10,y=300)

    Label(root,text='Hall',font='times 19 bold').place(x=150,y=400)
    ha=ttk.Combobox(root)
    ha['values']=['Hall 1 {50,000}',"Hall 2 {65,000}","Hall 3 {70,000}"]
    ha.current()
    ha.place(x=210,y=408,height=25,width=200)

    Label(root, text='Price', font='times 19 bold').place(x=150, y=500)
    ha1=Entry(root,bd=5)
    ha1.place(x=220, y=508,height=30,width=200)

    Label(root, text='Date', font='times 19 bold').place(x=150, y=600)
    da = Entry(root, bd=5)
    da.place(x=220, y=608, height=30, width=200)


    Label(root, text='Status', font='times 19 bold').place(x=150, y=700)
    ha2=ttk.Combobox(root)
    ha2['values']=['Paid','Un-Paid']
    ha2.place(x=225, y=708,height=25,width=200)

    Label(root,text='||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||\n||').place(x=550,y=350)
    Label(root,text='\n===================================================================='
                    '===================================================================='
                    '====================================================================').place(x=5,y=790)

    Label(root,text='Bill',font='times 20 bold underline').place(x=1000,y=340)

    def Bill():
        if len(e1.get()) > 0 and ((len(e2.get()) == 11) and (e2.get().isdigit() == True)) :
                Label(f, text='\tOrder Number : ', font="times 17 bold").place(x=0, y=50)
                Label(f, text='\tName  : ', font="times 17 bold").place(x=0, y=100)
                Label(f, text='\tContact Number : ', font="times 17 bold").place(x=0, y=150)
                Label(f, text='\tDate : ', font="times 17 bold").place(x=0, y=200)
                Label(f, text='\tPrice : ', font="times 17 bold").place(x=0, y=250)
                Label(f, text='\tDiscount : ', font="times 17 bold").place(x=0, y=300)
                Label(f, text='\tStatus : ', font="times 17 bold").place(x=0, y=350)

                Label(f, text=b_number, font="times 17 bold").place(x=350, y=50)
                Label(f, text=e1.get(), font="times 17 bold").place(x=350, y=100)
                Label(f, text=e2.get(), font="times 17 bold").place(x=350, y=150)
                Label(f, text=ha1.get(), font="times 17 bold").place(x=350, y=250)
                Label(f,text=da.get(),font="times 17 bold").place(x=350, y=200)
                Label(f, text=ha2.get(), font="times 17 bold").place(x=350, y=350)

                if (ha.get() == 'Hall 1 {50,000}') and int(ha1.get()) < 50000:
                    Label(f, text="Applied", font="times 17 bold").place(x=350, y=300)
                elif (ha.get() == 'Hall 2 {65,000}') and int(ha1.get()) < 65000:
                    Label(f, text="Applied", font="times 17 bold").place(x=350, y=300)
                elif (ha.get() == 'Hall 3 {70,000}') and int(ha1.get()) < 70000:
                    Label(f, text="Applied", font="times 17 bold").place(x=350, y=300)
                else:
                    Label(f, text="Not Available", font="times 17 bold").place(x=350, y=300)






        else:
            messagebox.showerror('Error',"Kindly Check \n1.Name\n2.Contact Number ")
    def clear():
        for widget in f.winfo_children():
            widget.destroy()

    def all():
        e1.delete(0, END)
        e2.delete(0, END)
        ha.delete(0, END)
        ha1.delete(0, END)
        ha2.delete(0, END)
        da.delete(0, END)
    def po():
        if len(e1.get()) > 0 and ((len(e2.get()) == 11) and (e2.get().isdigit() == True)):
            add_hall(b_number, f'{e1.get()}', int(e2.get()), f'{ha.get()}', ha1.get(), f'{da.get()}',f'{ha2.get()}')
            choice=messagebox.askyesno('Confirmation !','Place Order')
            if choice != 'No' :
                messagebox.showinfo('Confirmation','Order Placed !')
                clear()
                all()
            else:
                messagebox.askokcancel('Question ',"Place order or not !")
        else:
            messagebox.showerror('Error','Enter Valid \nName\nContact Number')






    Button(root,text="Bill",command=Bill,font='times 15 bold ',padx=25,pady=5).place(x=250,y=750)
    Button(root, text="Place Order",command=po, font='times 16 bold', bg='light grey', padx=45, pady=0).place(x=300, y=830)

    root.mainloop()
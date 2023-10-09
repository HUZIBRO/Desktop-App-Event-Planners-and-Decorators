import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import fun5
from fun5 import *

data=[]


def decorations():

    root=tk.Tk()
    root.title("Decoration Booking's ")
    root.attributes('-fullscreen',True)

    t = Frame(root,borderwidth=8)
    t.place(x=5,y=240,height=570,width=790)

    t1 = Frame(root, bd=8)
    t1.place(x=800, y=240, height=570, width=795)


    Label(root,text="S.H.M PLANNER'S AND DECORATOR'S  \n\nDECORATIONS'S BOOKINGS",font='times 21 bold').pack(side=TOP)

    Button(root,text='Exit',command=root.destroy,font='times 16 bold',bg='light grey',padx=45,pady=0).place(x=780,y=830)



    Label(root,text="Enter your Venue",font='times 18 bold ').place(x=70,y=150)
    ven=ttk.Combobox(root)
    ven['values']=['Custom',"Our Hall",'Custom Hall']
    ven.place(x=280,y=155,height=25,width=200)

    Label(root,text="Contact Number or order id ",font='times 18 bold').place(x=700,y=150)
    ch=Entry(root,bd=5)
    ch.place(x=1000,y=155,height=30,width=200)

    Label(root,text='=========================================================================================================================================================================================================================================================').place(x=5,y=220)


    def custom():

        Label(t,text="\"Order Details\"",font="algerian 18 underline").pack(side=TOP)

        Label(t,text="Name",font='times 15 bold').place(x=70,y=60)
        name=Entry(t,bd=5)
        name.place(x=230,y=60,height=30,width=200)

        Label(t,text='Contact Number',font='times 15 bold').place(x=70,y=120)
        cnum=Entry(t,bd=5)
        cnum.place(x=230,y=120,height=30,width=200)

        Label(t,text='Venue',font='times 15 bold ').place(x=70,y=180)
        v=Entry(t,bd=5)
        v.insert('end',ven.get())
        v.place(x=230,y=180,height=30,width=200)

        Label(t,text='Address',font='times 15 bold').place(x=70,y=240)
        add=Entry(t,bd=5)
        add.place(x=230,y=240,height=40,width=250)

        Label(t, text='Decoration', font='times 15 bold').place(x=70, y=300)
        dec = ttk.Combobox(t)
        dec['values']=['Normal [4500] '," Vip (Drinks,Flowers) [7000] ",'Custom' ]
        dec.place(x=230, y=300, height=30, width=250)

        Label(t, text='Date:', font='times 15 bold').place(x=70, y=360)
        d=Entry(t,bd=5)
        d.place(x=230, y=360, height=30, width=200)

        Label(t, text='Price', font='times 15 bold').place(x=70, y=420)
        pr = Entry(t, bd=5)
        pr.place(x=230, y=420, height=30, width=200)

        def po1():
            if len(name.get()) >0 or (len(cnum.get())!= 11 and cnum.get().isdigit == False) or len(add.get()) > 0 or len(dec.get()) > 0:
                mess=messagebox.askquestion('Confirmation','Are You Sure ')
                if mess == "yes":
                    fun5.add_dec_custom(f'{name.get()}', cnum.get(), f'{v.get()}', f'{dec.get()}', f'{d.get()}',pr.get(), f'{add.get()}')
                    messagebox.showinfo("Confirmed ",'Order placed')
                    clear1()
                    name.delete(0,END)
                    cnum.delete(0, END)
                    add.delete(0, END)
                    dec.delete(0, END)
                    d.delete(0, END)
                    v.delete(0, END)
                    pr.delete(0, END)

                else:
                    messagebox.showinfo('Cancelled !','Okay !')





        def bill():
            if len(name.get()) >0 or (len(cnum.get())!= 11 and cnum.get().isdigit == False) or len(add.get()) > 0:

                Label(t1,text='Bill',font='times 20 bold').pack(side=TOP)


                Label(t1,text='Name:',font='times 15 bold').place(x=70,y=75)
                Label(t1, text='Contact Number:', font='times 15 bold').place(x=70, y=150)
                Label(t1, text='Address:', font='times 15 bold').place(x=70, y=225)
                Label(t1, text='Decorations:', font='times 15 bold').place(x=70, y=300)
                Label(t1, text='Date:', font='times 15 bold').place(x=70, y=375)
                Label(t1, text='Price:', font='times 15 bold').place(x=70, y=450)

                Label(t1, text=name.get(), font='times 15 bold').place(x=230, y=75)
                Label(t1, text=cnum.get(), font='times 15 bold').place(x=230, y=150)
                Label(t1, text=add.get(), font='times 15 bold').place(x=230, y=225)
                Label(t1, text=dec.get(), font='times 15 bold').place(x=230, y=300)
                Label(t1, text=pr.get(), font='times 15 bold').place(x=230, y=450)
                Label(t1, text=d.get(), font='times 15 bold').place(x=230, y=375)

                Button(t1, text="Place Order",command=po1, font='times 16 bold', bg='light grey', padx=45, pady=0).place(x=300,y=500)



            else:
                messagebox.showerror('Error','Kindly Check the following : \n1. Name\n2. Contact Number\n3. Address')

        Button(t, text='Bill',command=bill, font='times 15 bold', padx=45, pady=0).place(x=250, y=500)










    def hall():
            Label(t, text="Order Details", font='times 18 bold').pack(side=TOP)
            Label(t, text="Name", font='times 15 bold').place(x=70,y=75)
            name = Entry(t, bd=5)
            name.place(x=200,y=75, height=30, width=200)

            Label(t, text='Contact Number', font='times 15 bold').place(x=70, y=150)
            cnum = Entry(t, bd=5)
            cnum.place(x=230, y=150, height=30, width=200)

            Label(t, text='Venue', font='times 15 bold ').place(x=70, y=225)
            ha=ttk.Combobox(t)
            ha['values'] = ['Hall 1 {50,000}', "Hall 2 {65,000}", "Hall 3 {70,000}"]
            ha.current()
            ha.place(x=200, y=225, height=30, width=200)


            Label(t, text='Decoration', font='times 15 bold').place(x=70, y=300)
            dec = ttk.Combobox(t)
            dec['values'] = ['Normal [4500] ', " Vip (Drinks,Flower's) [7000] ", 'Custom']
            dec.place(x=200, y=300, height=30, width=250)

            Label(t, text='Price', font='times 15 bold').place(x=70, y=375)
            pr = Entry(t, bd=5)
            pr.place(x=200, y=375, height=30, width=200)

            Label(t, text='Date', font='times 15 bold').place(x=70, y=450)
            d = Entry(t, bd=5)
            d.place(x=200, y=450, height=30, width=200)

            if c_h(ch.get()) == True:
                el = []
                if len(ch.get()) == 11:
                    curs.execute(f'select * from Hall_main where contact = {int(ch.get())}')
                    d2 = curs.fetchall()
                    for val in d2:
                        el.append(int(val[0]))
                        el.append(val[1])
                        el.append(int(ch.get()))
                        el.append(val[3])
                        el.append(int(val[4]))
                        el.append(val[5])
                        el.append(val[6])
                    name.insert('end', el[1])
                    cnum.insert('end', el[2])
                    ha.insert('end', el[3])
                    d.insert('end',el[5])
                elif len(ch.get()) != 11:
                    curs.execute(f'select * from Hall_main where orderid = {int(ch.get())}')
                    d3 = curs.fetchall()
                    for val in d3:
                        el.append(int(ch.get()))
                        el.append(val[1])
                        el.append(int(2))
                        el.append(val[3])
                        el.append(int(val[4]))
                        el.append(val[5])
                        el.append(val[6])
                    name.insert('end',el[1])
                    cnum.insert('end', el[2])
                    ha.insert('end', el[3])
                    d.insert('end', str(el[5]))
                    print(el)

                def po2():
                    if len(name.get()) >0 or (len(cnum.get())!= 11 and cnum.get().isdigit == False) or len(ha.get()) > 0 or len(dec.get()) > 0:
                        mess=messagebox.askquestion('Confirmation','Are You Sure ')
                        if mess == "yes":
                            fun5.add_dec(f'{ch.get()}', f'{dec.get()}', pr.get())
                            messagebox.showinfo("Confirmed ",'Order placed')
                            clear1()
                            name.delete(0,END)
                            cnum.delete(0, END)
                            ha.delete(0, END)
                            dec.delete(0, END)
                            d.delete(0, END)
                            pr.delete(0, END)

                        else:
                            messagebox.showinfo('Cancelled !','Okay !')





                def bill():
                    if len(name.get()) >0 or (len(cnum.get())!= 11 and cnum.get().isdigit == False) or len(dec.get()) > 0:

                        Label(t1,text='Bill',font='times 20 bold').pack(side=TOP)


                        Label(t1,text='Name:',font='times 15 bold').place(x=70,y=75)
                        Label(t1, text='Contact Number:', font='times 15 bold').place(x=70, y=150)
                        Label(t1, text='Venue:', font='times 15 bold').place(x=70, y=225)
                        Label(t1, text='Decorations:', font='times 15 bold').place(x=70, y=300)
                        Label(t1, text='Date:', font='times 15 bold').place(x=70, y=375)
                        Label(t1, text='Price:', font='times 15 bold').place(x=70, y=450)

                        Label(t1, text=el[1], font='times 15 bold').place(x=230, y=75)
                        Label(t1, text=el[2], font='times 15 bold').place(x=230, y=150)
                        Label(t1, text=el[3], font='times 15 bold').place(x=230, y=225)
                        Label(t1, text=dec.get(), font='times 15 bold').place(x=230, y=300)
                        Label(t1, text=pr.get(), font='times 15 bold').place(x=230, y=450)
                        Label(t1, text=el[5], font='times 15 bold').place(x=230, y=375)

                        Button(t1, text="Place Order",command=po2, font='times 16 bold', bg='light grey', padx=45, pady=0).place(x=300,y=500)



                    else:
                        messagebox.showerror('Error','Kindly Check the following : \n1. Name\n2. Contact Number\n3. Address')



                Button(t,text='Bill',command=bill,font='times 15 bold',padx=35,pady=0).place(x=250,y=500)
            else:
                messagebox.showerror('Error','Invalid Value Entered')


    def clear():
        for widget in t.winfo_children():
            widget.destroy()
    def clear1():
        for widget in t1.winfo_children():
            widget.destroy()

    def pro():
        if ven.get() == "Our Hall" and  len(ch.get()) > 0:
            clear()
            hall()
        elif ven.get() != "Our Hall":
            clear()
            custom()
        else:
            messagebox.showerror('Error',"Kindly Check Order number")

    Button(root,text="Proceed",command=pro,font='times 15 bold ',padx=45,pady=0).place(x=500,y=150)

    Label(root,
          text='=========================================================================================================================================================================================================================================================').place(
        x=5, y=810)





    root.mainloop()

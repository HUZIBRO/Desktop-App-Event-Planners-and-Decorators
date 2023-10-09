import tkinter as tk
from tkinter import *
import fun1
import fun2
from fun1 import *
from fun2 import *
import fun3
from fun3 import *
import fun4




root = tk.Tk()
root.title('S.H.M PLANNER\'S AND DECORATOR\'S ')
root.attributes('-fullscreen', True)
Label(root,text='S.H.M PLANNER\'S AND DECORATOR\'S',font='times 22 bold underline').pack(side=TOP)
Label(root).pack(side=TOP)
Label(root).pack(side=TOP)
def message1():
    Label(root,text="\"WE  ARE  HERE \nTO  MAKE  YOUR  EVENT  LOOK \nLIKE  AN  IMAGINATION\"",bg='Light blue',font='times 18 bold ').pack(side=TOP)
root.after(1200,message1)
def message2():
    Label(root,text=' ======> Book a Hall ----->> ',font='times 20 bold').place(x=120,y=250)
    Button(root,text='--- Book Hall ---',command=fun1.hall,font='times 16 bold',bg='light blue',padx=45,pady=0).place(x=650,y=250)

def m3():
    Label(root,text=' ======> Book a Decorator ----->> ',font='times 20 bold').place(x=120,y=400)
    Button(root,text='--- Book Decorator ---',command=fun2.decorations,font='times 16 bold',bg='light blue',padx=45,pady=0).place(x=650,y=400)

def m4():
    Label(root,text=' ======> View Hall Bookings  ----->> ',font='times 20 bold').place(x=120,y=550)
    Button(root,text='--- View Records ---',command=hr1,font='times 16 bold',bg='light blue',padx=45,pady=0).place(x=650,y=550)
def m5():
    Label(root,text=' ======> View Decoration Bookings ---->> ',font='times 20 bold').place(x=120,y=700)
    Button(root,text='--- View Records ---',command=fun4.hr,font='times 16 bold',bg='light blue',padx=45,pady=0).place(x=650,y=700)

root.after(2000, message2)
root.after(3000, m3)
root.after(4000, m4)
root.after(5000, m5)

Label().pack(side=BOTTOM)
Label().pack(side=BOTTOM)
Label().pack(side=BOTTOM)
Button(root,text='Exit',command=root.destroy,font='times 16 bold',bg='light grey',padx=45,pady=0).pack(side=BOTTOM)




root.mainloop()
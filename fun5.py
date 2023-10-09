import sqlite3
import pandas as pd
import numpy as np



cur= sqlite3.connect("mydatabase.db")

curs=cur



######## Here we are creating tables ############## 

def tables():
    curs.execute("create table Hall_main(orderid VARCHAR(250),name VARCHAR(250),contact VARCHAR(250),venue VARCHAR(250),price VARCHAR(250),date VARCHAR(250),status VARCHAR(250))")
    curs.execute("create table decoration(orderid VARCHAR(250),name VARCHAR(250),contact VARCHAR(250),venue VARCHAR(250),price VARCHAR(250),date VARCHAR(250),decoration VARCHAR(250))")
    curs.execute("create table dec_c(name VARCHAR(250),contact VARCHAR(250),venue VARCHAR(250),Decoration VARCHAR(250),date VARCHAR(250),price VARCHAR(250),address VARCHAR(250))")
    curs.commit()
    print("Tables created ")

tables()

def check_id(orderid):
    curs.execute(f"select  orderid from Hall_main where orderid = {int(orderid)} ")
    r = curs.fetchall()
    l = []

    for val in r:
        l.append(int(val[0]))

    if orderid in l:
        return True
    elif orderid not in l:
        return False

def check_num(num):
    curs.execute(f"select  contact from Hall_main where contact = {int(num)} ")
    r = curs.fetchall()
    l = []

    for val in r:
        l.append(int(val[0]))

    if num in l:
        return True
    elif num not in l:
        return False



def add_hall(o,n,c,v,p,d,s):
    curs.execute(f"insert into Hall_main(orderid,name,contact,venue,price,date,status) VALUES({o},'{n}',{int(c)},'{v}',{p},'{d}','{s}')")
    curs.commit()

def add_dec_custom(n,c,v,d,da,p,add):
    curs.execute(f"insert into dec_c(name,contact,venue,Decoration,date,price,address) VALUES('{n}',{int(c)},'{v}','{d}','{da}',{p},'{add}')")
    curs.commit()
def add_dec(o,dec,pr):
    if len(o) == 11:
        curs.execute(f"select * from Hall_main where contact ={int(o)}")
        data=curs.fetchall()
        li=[]

        for val in data:
            li.append(val[0])
            li.append(val[1])
            li.append(int(o))
            li.append(val[3])
            li.append(val[5])

        ord=li[0]
        na=li[1]
        con=int(o)
        hall=li[3]
        dat=li[4]
        de=dec
        price=int(pr)

        curs.execute(f"insert into decoration(orderid,name,contact,venue,price,date,decoration) VALUES({ord},'{na}',{int(con)},'{hall}',{price},'{dat}','{de}')")
        curs.commit()
    if len(o) != 11 :
        curs.execute(f"select * from Hall_main where orderid ={int(o)}")
        data=curs.fetchall()
        li=[]

        for val in data:
            li.append(int(o))
            li.append(val[1])
            li.append(int(val[2]))
            li.append(val[3])
            li.append(val[5])

        ord=int(o)
        na=li[1]
        con=int(li[2])
        hall=li[3]
        dat=li[4]
        de=dec
        price=pr

        curs.execute(f"insert into decoration(orderid,name,contact,venue,price,date,decoration) VALUES({ord},'{na}',{con},'{hall}',{price},'{dat}','{de}')")
        curs.commit()


def check_all_hall():
    pd.set_option('display.width', 320)
    pd.set_option('display.max_columns',10)
    r=pd.read_sql("select * from Hall_main  ",cur)
    re=pd.DataFrame(r)
    print(re)
"""
    curs.execute("select * from dec_c")
    c=curs.fetchall()
    l=[]
    for val in c:
        l.append(val[0])
        l.append(val[1])
        l.append(val[2])
        l.append(val[3])
        l.append(val[4])
        l.append(val[5])
        l.append(val[6])
    print(l)"""
def remove(inp):
    if len(inp) == 11:
        curs.execute(f"DELETE FROM Hall_main where contact = {inp} ")
        curs.commit()
    if len(inp) != 11:
        curs.execute(f"DELETE FROM Hall_main where orderid = {inp} ")
        curs.commit()

def remove_dec_c(i):
    curs.execute(f"DELETE FROM dec_c where contact = {int(i)} ")
    curs.commit()


def remove_dec(i):
    if len(i) <11:
        curs.execute(f"DELETE FROM decoration where orderid = {int(i)} ")
        curs.commit()
    else:
        curs.execute(f"DELETE FROM decoration where contact = {int(i)} ")
        curs.commit()


def c_h(q):
    if len(q) == 11:
        o=int(q)
        curs.execute(f"select contact from Hall_main where contact = {o}")
        data = curs.fetchall()
        l=[]
        for val in data:
            l.append(int(val[0]))

        if o in l:
            return True
        else:
            return False

    if len(q) != 11:
        o=int(q)
        curs.execute(f"select * from Hall_main where orderid ={int(o)}")
        data = curs.fetchall()
        l = []
        for val in data:
            l.append(int(val[0]))

        if o in l:
            return True
        else:
            return False

def c_d(q):
    if len(q) == 11:
        o=int(q)
        curs.execute(f"select contact from decoration where contact = {o}")
        data = curs.fetchall()
        l=[]
        for val in data:
            l.append(int(val[0]))

        if o in l:
            return True
        else:
            return False

    if len(q) != 11:
        o=int(q)
        curs.execute(f"select * from decoration where orderid ={int(o)}")
        data = curs.fetchall()
        l = []
        for val in data:
            l.append(int(val[0]))

        if o in l:
            return True
        else:
            return False

check_all_hall()
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
val=""
A=0
operator=""



def btn1_isclicked():
    global val
    val=val + "1"
    data.set(val)

def btn2_isclicked():
    global val
    val=val + "2"
    data.set(val)

def btn3_isclicked():
    global val
    val=val + "3"
    data.set(val)

def btn4_isclicked():
    global val
    val=val + "4"
    data.set(val)

def btn5_isclicked():
    global val
    val=val + "5"
    data.set(val)

def btn6_isclicked():
    global val
    val=val + "6"
    data.set(val)

def btn7_isclicked():
    global val
    val=val + "7"
    data.set(val)

def btn8_isclicked():
    global val
    val=val + "8"
    data.set(val)

def btn9_isclicked():
    global val
    val=val + "9"
    data.set(val)

def btn0_isclicked():
    global val
    val=val + "0"
    data.set(val)

def btn_plus_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="+"
    val=val+"+"
    data.set(val)


def btn_min_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="-"
    val=val+"-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="*"
    val=val+"*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="/"
    val=val+"/"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val
    A=0
    val=""
    operator=""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2=val
    if operator=="+":
        x=float(val2.split("+")[1])
        c=A+x
        data.set(c)
        val=str(c)

    elif operator=="-":
        x=float(val2.split("-")[1])
        c=A-x
        data.set(c)
        val=str(c)

    elif operator=="*":
        x=float(val2.split("*")[1])
        c=A*x
        data.set(c)
        val=str(c)
    
    elif operator=="/":
        x=float(val2.split("/")[1])
        if x==0:
            messgaebox.showerror("Error","scientific error")
            A=0
            val=""
            data.set(val)
        else:
            c=float(A/x)
            data.set(c)
            val=str(c)

#def result():
 #   global operator
  #  val=str(eval (operator))
   # data.set(val)
    #operator=""







cal=tk.Tk()
cal.geometry("300x400+300+300")
cal.resizable(0,0)
cal.title("Calculator")


data=StringVar()

lbl=Label(cal,text="label",anchor=SE,background="grey", font=("verdana",20),textvariable=data)#bg="grey"
#bg="#000000"
lbl.pack(expand=True,fill="both")


btnrow1=Frame(cal)
btnrow1.pack(expand=True, fill="both")

btnrow2=Frame(cal)
btnrow2.pack(expand=True, fill="both")

btnrow3=Frame(cal)
btnrow3.pack(expand=True, fill="both")

btnrow4=Frame(cal)
btnrow4.pack(expand=True, fill="both")


btn1=Button(btnrow1,text="1", font=("verdana", 22), relief=GROOVE, border=0,command=btn1_isclicked)
btn1.pack(side=LEFT, expand=TRUE, fill="both")

btn2=Button(btnrow1,text="2", font=("verdana", 22), relief=GROOVE, border=0,command=btn2_isclicked)
btn2.pack(side=LEFT, expand=TRUE, fill="both")

btn3=Button(btnrow1,text="3", font=("verdana", 22), relief=GROOVE, border=0, command=btn3_isclicked)
btn3.pack(side=LEFT, expand=TRUE, fill="both")

btn4=Button(btnrow1,text="+", font=("verdana", 22,"bold"), relief=GROOVE, border=0,command=btn_plus_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill="both")


btn1=Button(btnrow2,text="4", font=("verdana",22), relief=GROOVE, border=0,command=btn4_isclicked)
btn1.pack(side=LEFT, expand=TRUE, fill="both")

btn2=Button(btnrow2,text="5", font=("verdana",22), relief=GROOVE, border=0,command=btn5_isclicked)
btn2.pack(side=LEFT, expand=TRUE, fill="both")

btn3=Button(btnrow2,text="6", font=("verdana",22), relief=GROOVE, border=0,command=btn6_isclicked)
btn3.pack(side=LEFT, expand=TRUE, fill="both")

btn4=Button(btnrow2,text="-", font=("verdana",22,"bold"), relief=GROOVE, border=0, command=btn_min_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill="both")




btn1=Button(btnrow3,text="7", font=("verdana", 22), relief=GROOVE, border=0,command=btn7_isclicked)
btn1.pack(side=LEFT, expand=TRUE, fill="both")

btn2=Button(btnrow3,text="8", font=("verdana", 22), relief=GROOVE, border=0,command=btn8_isclicked)
btn2.pack(side=LEFT, expand=TRUE, fill="both")

btn3=Button(btnrow3,text="9", font=("verdana", 22), relief=GROOVE, border=0,command=btn9_isclicked)
btn3.pack(side=LEFT, expand=TRUE, fill="both")

btn4=Button(btnrow3,text="*", font=("verdana", 22,"bold"), relief=GROOVE, border=0, command=btn_mul_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill="both")





btn1=Button(btnrow4,text="C", font=("verdana", 22,), relief=GROOVE, border=0, command=c_pressed)
btn1.pack(side=LEFT, expand=TRUE, fill="both")

btn2=Button(btnrow4,text="0", font=("verdana", 22), relief=GROOVE, border=0,command=btn0_isclicked)
btn2.pack(side=LEFT, expand=TRUE, fill="both")

btn3=Button(btnrow4,text="=", font=("verdana", 22,"bold"), relief=GROOVE, border=0,command=result)
btn3.pack(side=LEFT, expand=TRUE, fill="both")

btn4=Button(btnrow4,text="/", font=("verdana", 22,"bold"), relief=GROOVE, border=0,command=btn_div_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill="both")






cal.mainloop()
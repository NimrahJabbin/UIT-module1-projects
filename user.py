import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("user")
#win.geometry("300x200+10+20")

name_label=ttk.Label(win,text="Enter your Name")
name_label.grid(row=0,column=0)
username=tk.StringVar()
nameEntry=ttk.Entry(win, width=20 , textvariable=username)
nameEntry.grid(row=0,column=1)

email_label=ttk.Label(win, text="Enter your Email")
email_label.grid(row=2,column=0)
useremail=tk.StringVar()
emailEntry=ttk.Entry(win, width=30, textvariable=useremail)
emailEntry.grid(row=2,column=1)


greet_label=ttk.Label(win, text="Hello unknown!!")
greet_label.grid(row=1,column=1)
def action():
    greet_label.configure(text="Hello "+ username.get())
btn=ttk.Button(win, text="submit", command=action)
btn.grid(row=0,column=2)


message_user=ttk.Label(win, text="We will send details on your Email")
message_user.grid(row=3,column=1)
def message():
    message_user.configure(text="We will send you details on "+ useremail.get())
btn2=ttk.Button(win, text="submit", command=message)
btn2.grid(row=2,column=2)


win.mainloop()
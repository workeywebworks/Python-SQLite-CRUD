import modules.config as cfg
import modules.insert as ist
import modules.query as qry
import tkinter 
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def save():
    conn = cfg.create_connection(cfg.database)
    ist.create(conn)
    qry.select_all(conn)

root = tkinter.Tk()
Label(root,text="Student ID").grid(row=0)
Label(root,text="Student Name").grid(row=1)
student_id=Entry(root)
student_name=Entry(root)
student_id.grid(row=0,column=1)
student_name.grid(row=1,column=1)
submit=Button(root,text="Submit",command=save)
submit.grid(row=2,column=1)
root.mainloop()



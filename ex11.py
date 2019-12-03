# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:21:05 2019

@author: Hadeel
"""
import tkinter as tk
from tkinter import Frame,BOTTOM,Button,LEFT,Label,Entry,messagebox,StringVar,scrolledtext,Menu,Toplevel
from tkinter import ttk,RIDGE,SUNKEN,mainloop,Listbox,IntVar,Checkbutton,W
from tkinter.colorchooser import *

#exercise 1 
"""
top = Tk()  
 
name = Label(top, text = "Name").grid(row=0,column=0)  
password = Label(top, text = "Password").grid(row=1,column=0) 
e1 = Entry(top).grid(row=0,column=1)  
e3 = Entry(top).grid(row=1,column=1)  
sumbit=Button(top,text='Submit').grid(row=4,column=0)  
top.mainloop()
"""
#exercise 2 

def open_child1():
    c=Toplevel(root)
    c.title("Child window 1")
    c.getmetry('200x160+230+130')
    #Label(c,text="Child window 1").grid()
    messagebox.showinfo("","This is a message")

    

def open_child2():
    c=Toplevel(root)
    c.title("Child window 2")
    c.getmetry('200x160+230+130')
    
    #Label(c,text="Child window 2").grid()
    
    lbl_number = Label(newChild,text="Enter Number")
    lbl_number.grid(row=0,column=0)

    txt_name=  StringVar()
    txt_input_number = Entry(newChild,textvariable=txt_name)
    txt_input_number.grid(row=0,column=1)



    lbl_name = Label(newChild,text="Password")
    lbl_name.grid(row=1,column=0)


    txt_name=StringVar()
    txt_input_name = Entry(newChild,textvariable=txt_name)
    txt_input_name.grid(row=1,column=1)


    btn = Button(newChild,text="Exit",command=exit_child)
    btn.grid(row=2,column=0)

def open_child3():
    c=Toplevel(root)
    c.title("Child window 3")
    c.getmetry('200x160+230+130')
    Label(c,text="Child window 3").grid()
    

root=Tk()
root.title('root window')
Button(root,text='Open Message',command=open_child1).grid()
Button(root,text='open child windoow 1',command=open_child2).grid()
Button(root,text='open child windoow 2',command=open_child3).grid()

root.mainloop()



#exercise 3
"""
window=Tk()
window.geometry('350x200')

def getColor():
    color=askcolor()
    color_name = color[1]  
    print(color_name)
    window.configure(background=color_name)
    
Button(text='Select Color',command=getColor).pack()
#window.configure(background=color[1])
mainloop()
"""
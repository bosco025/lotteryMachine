#!/usr/bin/env python
# coding: utf-8

from random import randint

def markSixV2():
    num = int(num_input.get())
    minN = int(minN_input.get())
    maxN = int(maxN_input.get())
    nums = []
    while len(nums) < num:
        randNum = randint(minN,maxN)
        if randNum not in nums:
            nums.append(randNum)
    nums.sort()
    output.config(text = nums)

from tkinter import *

# Initiate window + name
win = Tk() 
win.title("Mark-6-Generater") 

# Window Size (width x height)
win.geometry("500x400")
win.minsize(width=400, height = 200)
win.maxsize(width=500, height=400)

# Icon and color + transparent
#win.iconbitmap()
win.config(bg="Skyblue")
win.attributes("-alpha",0.9)
win.attributes("-topmost",1)

# Button
btn = Button(text="Generate", bg = "grey")
btn.config(width=5,height=2)

# Button add Command
btn.config(command = markSixV2)


# Label & Entry
title = Label(text = "Mark 6 Numbers Generator", bg = "sky blue", font="Microsoft 15")
lb = Label(text = "No. of numbers: ", bg = "white")
minlb = Label(text = "Min Number", bg = "white")
maxlb = Label(text = "Max Number", bg = "white")
num_input = Entry()
minN_input = Entry()
maxN_input = Entry()

output = Label(text="", bg = "light green")

title.pack()
lb.pack()
num_input.pack()
minlb.pack()
minN_input.pack()
maxlb.pack()
maxN_input.pack()
output.pack()
btn.pack()

win.mainloop()


# In[ ]:





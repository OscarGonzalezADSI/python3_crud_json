from tkinter import *

def Viewpadding(frame, registro):

    w_label = Label(frame, text="")
    w_label.config(bg="#000000")
    w_label.grid(row=registro, column=0)


def ViewTitle(frame, titleTable, registro, col, colspan):

    w_label = Label(frame, text=titleTable)
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=col, columnspan=colspan)


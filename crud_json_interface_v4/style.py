from tkinter import *


def StyleRoot(raiz):
    raiz.title("ventana de pruebas")
    raiz.iconbitmap("our_crud_lite.ico")
    raiz.geometry("300x350")
    raiz.config(bg="#000000")
    raiz.attributes("-fullscreen", True)
    raiz.wm_attributes('-alpha',0.8)
    raiz.overrideredirect(True)


def StyleFrame(miframe):

    miframe.config(bg="#000000", width=1200, height=600)


def Viewpadding(frame, registro):

    w_label = Label(frame, text="")
    w_label.config(bg="#000000")
    w_label.grid(row=registro, column=0)


def ViewTitle(frame, titleTable, registro, col, colspan):

    w_label = Label(frame, text=titleTable)
    w_label.config(bg="#000000", fg="#ffffff", font='Helvetica 12 bold')
    w_label.grid(row=registro, column=col, columnspan=colspan)




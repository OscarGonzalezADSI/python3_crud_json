from tkinter import *



master = Tk()

xx=StringVar()
yy=StringVar()


def Ubica(event):
    xx.set(event.x)
    yy.set(event.y)

def motion(event):
    xx.set(str(int(xx.get())+event.x))
    yy.set(str(int(yy.get())+event.y))
    master.geometry("300x300+"+str(xx.get())+"+"+str(yy.get()))
    print("Mouse position: (%s %s)" % (event.x, event.y))
    print(event.x)



whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<B1-Motion>', motion)
msg.bind('<Button-1>', Ubica)
msg.pack()
mainloop()
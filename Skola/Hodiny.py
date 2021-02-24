import tkinter
import time
import calendar
canvas = tkinter.Canvas(width=600,height=500)
canvas.pack()

cas = list(time.localtime(time.time()))

canvas.create_text(300, 50, text="Hodiny", font="Pursia 30 bold")

def mesiac():
    canvas.create_oval(110,135,190,265, fill="white")
    canvas.create_oval(130,145,195,255, fill="grey", outline="grey")

def slnko():
    canvas.create_oval(110,160,190,240, fill="yellow", outline="grey")
    canvas.create_line(150,135,150,157, width=3, fill="yellow")
    canvas.create_line(150,245,150,267, width=3, fill="yellow")

def hodiny():
    cas = list(time.localtime(time.time()))
    canvas.create_rectangle(100,125,500,275, fill="black")
    canvas.create_rectangle(105,130,195,270, fill="grey")
    canvas.create_rectangle(205,130,340,270, fill="grey")
    canvas.create_rectangle(360,130,495,270, fill="grey")
    canvas.create_oval(345,175,355,185, fill="lime")
    canvas.create_oval(345,215,355,225, fill="lime")
    if cas[3] > 7 and cas[3] < 19:
        slnko()
    else:
        mesiac()
    canvas.after(10,hodiny)
    
    if cas[3] < 10:
        canvas.create_text(272,200, text=str(0) + str(cas[3]), font="Pursia 60 bold", fill="lime")
    else:
        canvas.create_text(272,200, text=cas[3], font="Pursia 60 bold", fill="lime")
    
    if cas[4] < 10:
        canvas.create_text(427,200, text=str(0) + str(cas[4]), font="Pursia 60 bold", fill="lime")
    else:
        canvas.create_text(427,200, text=cas[4], font="Pursia 60 bold", fill="lime")
        
    canvas.create_text(300,400,text=str(cas[2]) + " . " + str(cas[1]) + " . "  + str(cas[0]), font="Pursia 35 bold")
    
def kalendar():
    kal = calendar.month(cas[0], cas[1])
    print(kal)

kalendar()
hodiny()

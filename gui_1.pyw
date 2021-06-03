from tkinter import Tk, Button, Label, DoubleVar, Entry,StringVar

win = Tk()

win.title("F2M App")
win.configure(background="#55efc4")
win.geometry("350x250")
win.resizable(width=False,height=False)


def convert():
    val = float(ft_entry.get())
    meter = val*0.3048
    mt_val.set("%.2f"%meter)

def clear():
    ft_val.set(" ")
    mt_val.set(" ")


ft_lb = Label(win,text="Feet",bg="purple",fg="white",width=14)
ft_lb.grid(column =0,row=0,padx=15,pady=15)

ft_val = DoubleVar()
ft_entry = Entry(win,textvariable=ft_val,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

mt_lb = Label(win,text="Meter",bg="brown",fg="white",width=14)
mt_lb.grid(column =0,row=1,padx=15,pady=15)

mt_val = DoubleVar()
mt_entry = Entry(win,textvariable=mt_val,width=14)
mt_entry.grid(column=1,row=1)
mt_entry.delete(0,'end')

cnvert_btn = Button(win,text="Convert",bg="blue",fg="white",width=14,command=convert)
cnvert_btn.grid(column=0,row=3,padx=15)

clear_btn = Button(win,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

win.mainloop()

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
root = Tk()


def parameters():
    energy_show = Label(root, text='Энергия', font=("Arial Bold", 40), bg='grey')
    energy_show.place(x=10, y=10, width=300, height=100)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("blue.Horizontal.TProgressbar", background='blue')
    energy_bar = Progressbar(root, length=200, style='blue.Horizontal.TProgressbar')
    energy_percent = 70
    energy_bar['value'] = energy_percent
    energy_bar.place(x=60, y=120)
    money_show = Label(root, text='Деньги', font=('Arial Bold', 40), bg='grey')
    money_show.place(x=310, y=10, width=300, height=100)
    money = 10000
    money_count = Label(root, text=str(money) + ' галактов', font=("Arial Bold", 14), bg='grey')
    money_count.place(x=310, y=102, width=300, height=50)

panelFrame = Frame(root, width=1920, height=1080, bg='grey')
panelFrame.place(x=0, y=0)

parameters()
root.mainloop()

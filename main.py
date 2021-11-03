from deep_translator import (GoogleTranslator)
import random
from tkinter import *
from tkinter import ttk

lenguajes = GoogleTranslator.get_supported_languages()

s = ttk.Style()
s.theme_use('clam')

def clicked():

    log = []
    log_lan = []
    def log_fun():
        print(log)
        listbox = ttk.Treeview(window,column=("c1","c2"),show="headings",height=5)
        listbox.column("# 1", anchor=CENTER)
        listbox.heading("# 1", text="Idioma")
        listbox.column("# 2", anchor=CENTER)
        listbox.heading("# 2", text="Texto")

        for i in range(len(log)):
            listbox.insert("","end",text="1",values=(log_lan[i],log[i]))

        listbox.grid(column=4,row=4)


    translated = txt.get()
    log.append(translated)
    log_lan.append("spanish")
    veces = int(num.get())

    for i in range(veces):
        lan = random.choice(lenguajes)
        translated = GoogleTranslator(source='auto', target=lan).translate(text=translated)
        log.append(translated)
        log_lan.append(lan)

    translated = GoogleTranslator(source='auto', target="es").translate(text=translated)
    log.append(translated)
    log_lan.append("spanish")
    print(translated)
    lbl.configure(text=translated)

    btn_log= Button(window,text="Mostrar registro", command=log_fun)
    btn_log.grid(column=3,row=5)

window = Tk()

window.title("Traductor")

window.geometry('700x350')

lbl1 = Label(window, text="Texto", font=("Arial Bold",15))

lbl1.grid(column=1, row=2)

txt = Entry(window,width=20)

txt.grid(column=2,row=2)

lbl1 = Label(window, text="Veces", font=("Arial Bold",15))

lbl1.grid(column=1, row=3)

num = Scale(window, from_=1, to=50, orient=HORIZONTAL)
num.grid(column=2,row=3)

btn = Button(window, text="Traducir", command=clicked)

btn.grid(column=2, row=4)

lbl = Label(window, font=("Arial Bold",15))

lbl.grid(column=2, row=5)

window.mainloop()









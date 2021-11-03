from deep_translator import (GoogleTranslator)
import random
from tkinter import *

lenguajes = GoogleTranslator.get_supported_languages()


def clicked():
    log = []
    def log_fun():
        print(log)
        listbox = Listbox(width=50)
        listbox.insert(0, *log)
        listbox.grid(column=3,row=4)
    translated = txt.get()
    log.append(translated)
    veces = int(num.get())
    for i in range(veces):
        translated = GoogleTranslator(source='auto', target=random.choice(lenguajes)).translate(text=translated)
        log.append(translated)
    translated = GoogleTranslator(source='auto', target="es").translate(text=translated)
    log.append(translated)
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









from deep_translator import (GoogleTranslator)
import random
from tkinter import *

lenguajes = GoogleTranslator.get_supported_languages()


def clicked():
    translated = txt.get()
    veces = int(num.get())
    for i in range(veces):
        translated = GoogleTranslator(source='auto', target=random.choice(lenguajes)).translate(text=translated)

    translated = GoogleTranslator(source='auto', target="es").translate(text=translated)
    print(translated)
    lbl.configure(text=translated)

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

lbl = Label(window, font=("Arial Bold",20))

lbl.grid(column=2, row=5)

window.mainloop()









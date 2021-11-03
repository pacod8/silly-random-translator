from deep_translator import (GoogleTranslator)
import random


lenguajes = GoogleTranslator.get_supported_languages()

translated = input("Que quieres traducir?: ")
veces = int(input("Cuantas veces?: "))

for i in range(veces):
    translated = GoogleTranslator(source='auto', target=random.choice(lenguajes)).translate(text=translated)

translated = GoogleTranslator(source='auto', target="es").translate(text=translated)
print(translated)

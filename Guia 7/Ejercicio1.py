# Ejercicio 1:
from cgitb import text
import os
os.system("cls")

from colorama import init, Fore
init(True)

#1 A partir de una cadena de texto iniciada en el código, mostrar la cadena//
#  en color azul.
texto = "Meta empresa, propietaria de Facebook y de Instagram, ha donado 300.000 dólares a la " \
"Python Software Foundation (PSF), el grupo que reúne a los principales desarrolladores del lenguaje" \
"de programación Python y que mantiene el Core Python (CPython), el lenguaje de programación de código" \
"abierto que impulsa la mayoría de las aplicaciones de aprendizaje automático e inteligencia artificial."

print(Fore.BLUE + texto)

#2 Crear un nuevo_texto con los caracteres que sean solo letras y espacios,//
#  mostrar nuevo_texto en color blanco (aplicar join combinado con sintaxis//
#  por comprensión para filtrar o filter).
nuevo_texto = " "

for caracter in texto:
    if caracter.isalpha() or caracter.isspace():
        nuevo_texto += caracter

print("\n","Nuevo texto con solo letras y espacios: ")
print(Fore.WHITE + nuevo_texto)

# Convertir el texto en una lista de palabras y mostrar todos los elementos//
#  y su posición en color blanco (enumerate).

print("\n","Lista palabras y su posición:")
palabras = nuevo_texto.split()

for indice, valor in enumerate(palabras):
    print(indice,valor)

# Encontrar y mostrar el elemento menor, mayor y su posición en la lista //
# de palabras (min, max e index, min y max deben proporcionar el argumento //
# key = len para comparar cadenas).
menor = min(palabras,key= len)
mayor = max(palabras, key= len)
print()
print("Palabra de menor longitud", menor, ",en la posición", palabras.index(menor))
print("Palabra de menor longitud", mayor, ",en la posición", palabras.index(mayor))

# Mostrar la lista con formato de texto en color blanco, una palabra al lado77
#  de la otra separada por un espacio (join).

print("\n", Fore.WHITE + " ".join(palabras))

# Mostrar la palabra menor en rojo en cada aparición, contar cuantas //
# apariciones tiene.
contador= 0
for palabra in palabras:
    if palabra == menor:
        contador += 1
        print(Fore.RED + palabra, end=" ")
    else:
        print(Fore.WHITE + palabra, end=" ")
print()
print("La palabra menor aparce" , contador ,"veces.")
print()
# Mostrar la palabra mayor en verde en cada aparición, contar cuantas//
#  apariciones tiene.Mostrar cuántas palabras menores y cuántas mayores se encontraron.

contador2= 0
for palabra in palabras:
    if palabra == mayor:
        contador2 += 1
        print(Fore.GREEN + palabra, end=" ")
    else:
        print(Fore.WHITE + palabra, end=" ")
print()
print("La palabra mayor aparece" , contador2 , "vez.")



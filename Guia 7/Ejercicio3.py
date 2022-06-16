# Ejercicio 3:
# A partir de una cadena de texto inicializada en el código, convertir a //
# una lista p de palabras y mostrar.
texto = "Meta empresa, propietaria de Facebook y de Instagram, ha donado 300.000 dólares a la " \
"Python Software Foundation (PSF), el grupo que reúne a los principales desarrolladores del lenguaje" \
"de programación Python y que mantiene el Core Python (CPython), el lenguaje de programación de código" \
"abierto que impulsa la mayoría de las aplicaciones de aprendizaje automático e inteligencia artificial."
print("Texto lista:")
p = texto.split()
print(p)

# Mostrar el elemento menor (en cantidad de caracteres), mayor//
#  (en cantidad de caracteres) y su posición en la lista p //
# (aplicar min y max con el parámetro key = len)
# ejemplo: menor = min(palabras, key = len).
print()
menor = min(p,key= len)
print()
mayor = max(p, key= len)
print()
print("Palabra de menor longitud", menor, ",en la posición", p.index(menor))
print("Palabra de menor longitud", mayor, ",en la posición", p.index(mayor))

# Concatenar los elementos de la lista en una nueva cadena nuevo_texto pero//
#  en sentido inverso, es decir donde el primer elemento sea el último //
# elemento de p y mostrar al finalizar (aplicar join con for reversed).
print("\n", "Texto invertido:")
nuevo_texto = " ".join(reversed(p))
print(nuevo_texto)
print()

# Crear una función para mostrar la lista p, llamar desde main.
def mostrar_lista(lista):
    for elemnto in lista:
        print(elemnto, end= " ")

print("\n", "Texto lista:")
mostrar_lista(p)

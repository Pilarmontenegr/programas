# Ejercicio 2- Guia 7:
import random

# 1 Generar una lista de 30 elementos enteros al azar entre 50 y 250 //
# inclusivos y guardarlos en una lista v1 (random.sample).
v1 = random.sample(range(50,251),30)
print("v1",v1)

#2  Hacer una copia en una segunda lista v2 con los valores del primero //
# que se encuentren entre 75 y 225 (aplicar sintaxis por comprensión).
v2 = [numero for numero in v1 if numero>= 75 and numero<=225]
print("\n","v2",v2)

#3 Crear una función para mostrar todos los elementos de una lista cualquiera//
#  y su posición, llamarla desde el main para mostrar v1 y v2.
def mostrar_lista(lista):
    for indice, valor in enumerate(lista):
        print(indice, valor)

print("\n","Elementos y su posición de v1" )
mostrar_lista(v1)
print("\n","Elementos y su posición de v2" )
mostrar_lista(v2)

#4 Crear una función para encontrar el mayor, menor y el promedio de un //
# vector cualquiera, llamar desde el main para mostrar los resultados de //
# v1 y v2.
def enocntrar_mayor_menor (lista):
    menor = min(lista)
    mayor=max (lista)
    promedio = sum(lista) / len(lista)
    print(f"El menor elemento es {menor} y el mayor es {mayor}, el promedio es {promedio}.")

print("\n", "Lista v1:")
enocntrar_mayor_menor(v1)
print("\n", "Lista v2:")
enocntrar_mayor_menor(v2)

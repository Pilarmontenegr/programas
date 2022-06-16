# Ejercicio 8:
# 1 Generar un vector de 30 números enteros al azar de 2 dígitos.
from itertools import count
from logging.config import valid_ident
import random
vector1 = random.sample(range(10,100),30)
# 2 Mostrar lista.
print("Vecotor 1: ",vector1)
print()

# 3 Ordenar y mostrar la lista.
vector1.sort()
print("Vector ordenado: " ,vector1)
print()

# 4 Encontrar el valor promedio.
promedio= sum(vector1) / len(vector1)

# 5 Mostrar el valor promedio.
print("Promedio: ",promedio)
print()

# 6 Encontrar el valor por encima y por debajo del valor promedio.
valor_mayor_promedio =0
valor_menor_promedio= 0

for numero in vector1:
    if numero <promedio:
        valor_menor_promedio = numero
    if numero >promedio:
    
        valor_mayor_promedio = numero
        break

# 7 Mostrar los valores por encima y por debajo del promedio.
print("Elemento mayor que el promedio: ",valor_mayor_promedio, " en la posición: "
,vector1.index(valor_mayor_promedio))
print()
print("Elemento menor que el promedio: ",valor_menor_promedio, " en la posición: "
,vector1.index(valor_menor_promedio))
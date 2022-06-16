# Ejercicio 7:
#1- Generar un vector de 30 números enteros al azar de 2 dígitos.

import random
lista = random.sample(range(10,100),30)

print(lista)
print()
#2- Mostrar cada elemento y su posición (enumerate).

for indice,valor in enumerate(lista):
    print("Indice: ",indice,",Valor: ",valor)
print() 
#3 Encontrar el elemento menor y su posición por arriba del valor 50 //
# (aplicar sintaxis por comprensión o filter).

#(min devuelve el valor menor de los menores a 50)

menor = min([valor for valor in lista if valor >50])

print("Utilizando función generadora, El valor menor por arriba de 50 es: ",menor,
" Se encuentra en la posición", lista.index(menor))

menor2 = min(filter(lambda x: x> 50, lista))
print("Utilizando función filtradora, El valor menor por arriba de 50 es: ",menor,
" Se encuentra en la posición", lista.index(menor))
print()
#4 Encontrar el elemento mayor y su posición por debajo del valor 50 //
# (aplicar sintaxis por comprensión o filter).

mayor = max([valor for valor in lista if valor <50])
 
print("Utilizando función generadora, El valor mayor por debajo de 50 es: ",mayor,
" Se encuentra en la posición", lista.index(mayor))

mayor2 = max(filter(lambda x: x< 50, lista))

print("Utilizando función filtradora, El valor mayor por debajo de 50 es: ",mayor,
" Se encuentra en la posición", lista.index(mayor))

# Ejercicio 4:
# 1 Crear un código para ingresar n valores decimales entre 1 y 100, salir con//
#  cero.Almacenar en un vector.
v1 =[]

while True:
    n = float(input("Ingrese un número entre 1 y 100: "))

    if n == 0:
        break
    
    if n>100 or n<1 :
        print("Número fuera de rango.")
        continue

    print("Número dentro de rango.")
    v1.append(n)
# 2 Guardar los valores ingresados en una lista v1 y hacer una copia en una //
# segunda lista v2 con los valores del primero que sean mayor a 50 //
# (sintaxis por comprensión).
print()
v2 = 0
v2 = [numero for numero in v1 if numero>50]
print("Valores mayores a 50:")
print(v2)
print()
# 3 Crear una función para mostrar todos los elementos de un vector//
#  cualquiera y su posición, llamarla desde el main para mostrar v1 y v2.
def mostrar_elementos(lista):
    for indice,valor in enumerate(lista):
        print(indice,valor)

print("\n", "Mostramos indice y valor de v1:")
mostrar_elementos(v1)

print("\n", "Mostramos indice y valor de v2:")
mostrar_elementos(v2)

# Crear una función para encontrar el mayor menor y el promedio de una //
# lista cualquiera, llamar desde el main para mostrar los resultados de v1 //
# y v2.
def mostrar (lista):
    if len(lista) ==0:
        return 0,0,0

    menor = min(lista)
    mayor =max (lista)
    promedio = sum(lista) / len(lista)
    return menor,mayor,promedio

print()
print("v1")
a,b,c = mostrar(v1)
if c==0:
    print("No hay datos para procesar en v1.")
else:
    print(f"Menor:{a}, mayor {b}, promedio {c} ")

print()
print("v2")
a,b,c = mostrar(v2)
if c==0:
    print("No hay datos para procesar en v2.")
else:
    print(f"Menor:{a}, mayor {b}, promedio {c} ")
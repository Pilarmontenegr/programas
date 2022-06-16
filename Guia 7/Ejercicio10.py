# Ejercicio 10
# 1 Desarrollar una función que reciba como parámetro una lista de valores y//
#  encuentra la moda (es el valor que aparece más veces dentro del conjunto)
from pdb import lasti2lineno


def moda(lista):
    # 2 Mostrar la lista original.
    print("Lista original ",lista)
    print()
    #3 Ordenar y mostrar la lista de nuevo.
    lista.sort()
    print("Lista ordenada: ", lista)
    print()

    # 4 Escribir el algoritmo para encontrar y mostrar la moda según el //
    # siguiente cuadro:
    duplicados = []

    for indice, elemento in enumerate(lista):
        if indice < (len(lista)-1) and elemento in lista[indice +1:] and elemento not in duplicados:
            duplicados.append(elemento)

    match len(duplicados):
        case 0:
            print("Amodal: ",duplicados)
        case 1:
            print("Moda: ",duplicados)
        case 2:
            print("Bimodal: ",duplicados)
        case _:
            print("Multimodal: ",duplicados)

# 5 Llamar desde el main la función con una lista par y otra impar en //
# cantidad de elementos.
v1 = [7,2,5,5,9,10]
moda(v1)
print("_______________________________________________________________________")
v2 =[3,2,3,9,7,8,5,9]
moda(v2)
print("_______________________________________________________________________")
v3= [9,3,3,5,7,7,8,9,2]
moda(v3)
print("_______________________________________________________________________")
v4 = [9,4,5,7,2]
moda(v4)
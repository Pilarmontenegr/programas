# Ejercicio 9 :
#1 Desarrollar una función que reciba como parámetro una lista de valores y //
# encuentre la mediana (Es el valor que se encuentra en el medio de la lista//
#  ordenada).
def encotrar_mediana(lista):
    #2 Mostrar la lista original.
    print("Lista original ",lista)
    print()
    #3 Ordenar y mostrar la lista de nuevo.
    lista.sort()
    print("Lista ordenada: ", lista)
    print()
    #4 En caso de que la lista contenga una cantidad de valores impares la //
    # mediana es el valor central.
    if len(lista) % 2 != 0: #osea es impar
        indice_medio = len(lista) //2 #toma la parte entera,justo la del medio
        mediana = lista[indice_medio]

    #5 En caso de que la lista contenga una cantidad de valores pares la mediana //
    # se calcula tomando los dos valores centrales se suman y dividen por dos.
    else: #es par
        indice_medio1 =(len(lista) //2) -1 #tomo el valor de la izquierda desde el medio
        indice_medio2 = indice_medio1 +1 # tomo el valor de la derecha desde el medio

        mediana = (lista[indice_medio1] + lista[indice_medio2]) /2


    #6  Mostrar el valor de la mediana indicando si lista es par o impar en //
    # cantidad de elementos.
    print("Mediana ", mediana)
    print()

    if len(lista) %2 ==0:
        print("La lista es par.")
    else:
        print("La lista es impar.")

#7 Llamar desde el main la función con una lista par y otra impar en //
# cantidad de elementos.
lista1 = [2,5,8,11,16,21,30]

encotrar_mediana(lista1)
print("_________________________________________________________________________")

lista2= [3,10,36,255,79,24,5,8]

encotrar_mediana(lista2)
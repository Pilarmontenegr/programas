# Ejercicio 5:
# Permitir el ingreso de una serie de temperaturas entre -60 y 60 //
# (no debe permitir valores fuera del rango).
contador_menor_0= 0
acumulador_menor= 0
contador_mayor_0= 0
acumulador_mayor= 0
menor= 100
mayor= -100
while True:
    temperatura = int(input("Ingrese una temperatura entre -60 y 60 inclusivos: "))

    # Salir con 100.
    if temperatura== 100:
        break

    if temperatura< -60 or temperatura >60:
        print("Valor fuera de rango.")
        continue

# Obtener la cantidad y promedio de las lecturas menores a cero grados.
    if temperatura<0:
        contador_menor_0 +=1
        acumulador_menor += temperatura

# Obtener la cantidad y promedio de las lecturas mayores o igual a cero//
#  grados.
    if temperatura>=0:
        contador_mayor_0 +=1
        acumulador_mayor +=temperatura
# Obtener la lectura menor y mayor de la serie.
    if temperatura < menor:
        menor = temperatura
    if temperatura >mayor:
        mayor = temperatura

print()
if contador_mayor_0 + contador_menor_0 == 0:
    print("No se ingresaron temperaturas.")
else:
    print("Temperaturas menores a 0: ",contador_menor_0)
    print("Temperaturas mayores o igual a 0: ",contador_mayor_0)

    if contador_menor_0 >0:
        print("\n","Promedio de temperaturas menores a cero: ", acumulador_menor / contador_menor_0)
    if contador_mayor_0 >0:
        print("\n","Promedio de temperaturas mayores o igual a cero: ", acumulador_mayor / contador_mayor_0)

    print("\n",f"Temperatura menor:{menor} ")
    print(f"Temperatura mayor:{mayor} ")




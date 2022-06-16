# Ejercicio 6:
# A partir de una cadena de texto (no pueden ser todas mayúsculas) realizar//
#  cada punto y mostrar el resultado en pantalla.
texto = "Python.exe, también conocido como un archivo Windows Executable, "\
    "fue creado por PortableApps para el desarrollo de OpenOffice.org Portable"\
     "3.2. Los archivos de EXE se incluyen en la categoría de tipo de archivo "\
    "de Win32 EXE (Windows Executable)."
print(texto)
print()
# Colocar la palabra en una lista (Split).
lista = texto.split()
print(lista)
print()

# Desarrollar un bucle while para el ingreso de una palabra a buscar en la//
#  lista.
palabra = ""
while True:
    palabra = input("Ingrese una palabra a buscar en la lista: ")

    # Salir cuando no se ingrese ningún valor (Enter).
    if palabra == "":
        break

    # Buscar la palabra en la lista y mostrar si se encontró o no, y su //
    # posición en la lista.
    if palabra in lista:
        print("La palabra se encuentra en la posición ", lista.index(palabra))
    else:
        print("La palabra no se encuentra en la lista.")
# 6 Unir el vector en una nueva cadena con el primer carácter en mayúscula y//
#  el resto como está originalmente (Join, capitalize).
print()
nuevo_texto = " ".join([p.capitalize() for p in lista])
print("\n","Nuevo texto con primer caracter en mayuscula: ",nuevo_texto)

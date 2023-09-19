import time
import random
def opcion_1():

    def llenar_arreglo(longitud):
        arreglo = []
        for i in range(longitud):
            elemento = int(input(f"Ingrese el elemento {i + 1}: "))
            arreglo.append(elemento)
        return arreglo

    try:
        longitud = int(input("Ingresa la longitud deseada del arreglo: "))
    
        if longitud <= 0:
            print("La longitud del arreglo debe ser un número positivo.")
        else:
            arreglo = llenar_arreglo(longitud)
            print(f"Arreglo ingresado: {arreglo}")
    except ValueError:
        print("Por favor, ingresa una longitud válida (un número entero positivo).")

    inicio = time.time()

    def burbuja(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    burbuja(arreglo)

    fin = time.time()

    tiempo_transcurrido = fin - inicio

    print("Arreglo ordenado:", arreglo)
    print("Tiempo transcurrido en segundos:", tiempo_transcurrido)


    
def opcion_2():

    def llenar_arreglo(longitud):
        arreglo = []
        for i in range(longitud):
            elemento = int(input(f"Ingrese el elemento {i + 1}: "))
            arreglo.append(elemento)
        return arreglo

    try:
        longitud = int(input("Ingresa la longitud deseada del arreglo: "))
    
        if longitud <= 0:
            print("La longitud del arreglo debe ser un número positivo.")
        else:
            arreglo = llenar_arreglo(longitud)
            print(f"Arreglo ingresado: {arreglo}")
    except ValueError:
        print("Por favor, ingresa una longitud válida (un número entero positivo).")

    inicio = time.time()

    def burbuja_op(lista):
        n = len(lista)
        for i in range(n):
            intercambiado = False
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    intercambiado = True
            if not intercambiado:
                break

    burbuja_op(arreglo)

    fin = time.time()

    tiempo_total = fin - inicio
    print("El arreglo ordenado:", arreglo)
    print("El tiempo transcurrido en segundos:", tiempo_total)

    


def menu():
    while True:
        print("Menú:")
        print("1. Método de burbuja")
        print("2. Método de burbuja optimizado")
        print("3. Salir")
        
        seleccion = input("Seleccione una opción: ")
        
        if seleccion == '1':
            opcion_1()
        elif seleccion == '2':
            opcion_2()
        elif seleccion == '3':
            print("Nos vidrios diria el ciego")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()

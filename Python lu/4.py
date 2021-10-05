"""Elabore un algoritmo que almacene 10 números enteros en una lista y en otra almacene el cubo de los numeros de la primera lista"""

try:
    lista = []
    lista2= []

    for i in range(10):
        num = int(input("Digite un número: "))
        lista.append(num)
        
    print("La lista es ", lista)

    for i in range(len(lista)):
        cubo =lista[i]**3
        lista2.append(cubo)

    print(lista2)

except ValueError:
    Print("Error")
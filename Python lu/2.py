"""2 Elabore un algoritmo que almacene 15 números enteros en una lista, imprima la posición donde se encuentra el número mayor"""

try:
    lista = []
    mayor = 0
    pos = 0

    for i in range(15):
        num = int(input("Digite un número: "))
        lista.append(num)
    print("La lista es ", lista)

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            pos = i
    print("La posición del número mayor es: ", pos)

except ValueError:
    Print("Error")
    
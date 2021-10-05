"""1. Elabore un algoritmo que almacene una lista de 10 elementos, imprima la lista

Lista = [46,78,23,1,0,5,67,33,29] """

try:
    lista = []
    for i in range(10):
        num = int(input("Digite un número: "))
        lista.append(num)
    print("La lista es: ", lista)

except ValueError:
    Print("Error")
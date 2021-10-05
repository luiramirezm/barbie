"""Elabore un algoritmo que almacene 20 numeros en una lista. imprima la sumatoria de los números de la lista"""

try:
    lista = []
    suma = 0

    for i in range(20):
        num = int(input("Digite un número: "))
        lista.append(num)
    print("La lista original es ", lista)

    for i in range (len(lista)):
        suma = lista[i] + suma
         
        
    print("La suma de la lista es: ", suma)
  

except ValueError:
    Print("Error")
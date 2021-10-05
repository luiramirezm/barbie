"""5. crear un programa q almacene 10 numeros enteros en una lista y que los muestre en otra lista en orden inverso"""

try:
    lista = []

    for i in range(10):
        num = int(input("Digite un número: "))
        lista.append(num)
        
    print("La lista original es ", lista)
    print("La lista invertida es: ", list(reversed(lista)))

except ValueError:
    Print("Error")
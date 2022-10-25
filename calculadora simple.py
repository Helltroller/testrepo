print("Esta es una calculadora basica\n")
print("Escoge una opcion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division Entera")
print("6. Modulo")
print("7. Exponencia\n")

loop = True
while loop:
    numero = int(input("Escoge una opcion:\n"))
    if numero == 1:
        print("Elegista una suma.\n")
        numero = int(input("Dame el primer valor: "))
        numero += int(input("Dame el segundo valor: "))
        print("El resultado es: ", numero,"\n")
    elif numero == 2:
        print("Elegista una resta.")
        numero = int(input("Dame el primer valor: "))
        numero -= int(input("Dame el segundo valor: "))
        print("El resultado es: ", numero,"\n")
    elif numero == 3:
        print("Elegista una multiplicacion.")
        numero = int(input("Dame el primer valor: "))
        numero *= int(input("Dame el segundo valor: "))
        print("El resultado es: ", numero,"\n")    
    elif numero == 4:
        print("Elegista una division.")
        numero = float(input("Dame el primer valor: "))
        numero /= float(input("Dame el segundo valor: "))    
        print("El resultado es: ",round(numero,1),"\n")
    elif numero == 5:
        print("Elegista una division entera.")
        numero = int(input("Dame el primer valor: "))
        numero //= int(input("Dame el segundo valor: "))
        print("El resultado es: ", round(numero,1),"\n")
    elif numero == 6:
        print("Elegista una modulo.")
        numero = float(input("Dame el primer valor: "))
        numero %= float(input("Dame el segundo valor: "))
        print("El resultado es: ", round(numero,1),"\n")
    elif numero == 7:
        print("Elegista una exponencia.")
        numero = int(input("Dame el primer valor: "))
        numero **= int(input("Dame el segundo valor: "))
        print("El resultado es: ", numero,"\n")
    else:
        loop = False

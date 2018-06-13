quantity = int(input())

for i in range (quantity) :
    entrada = list(input())
    numero1 = int(entrada[0])
    numero2 = int(entrada[2])
    operation = entrada[1]

    if numero1 == numero2 :
        print(numero1**2)
    elif operation == operation.lower() :
        print(numero2 + numero1)
    else :
        print(numero2 - numero1)

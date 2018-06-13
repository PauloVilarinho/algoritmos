def main():
    numero_a = int(input("digite o numero 1: "))
    numero_b = int(input("digite o numero 2: "))

    a = numero_a
    b = numero_b
    resto = a % b

    while resto != 0 :
        resto = a % b
        a = b
        b = resto


    print(a)


if __name__ == '__main__':
    main()

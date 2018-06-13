def main():
    numero =  int(input("difite o nuemro 1: "))
    aux =  1
    digitos = 0
    while numero//aux > 0 :
        aux *= 10
        digitos += 1

    print(digitos)

if __name__ == '__main__':
    main()

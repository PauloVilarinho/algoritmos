def main():
    n = int(input("digite o numero"))
    aux = 1
    valor = 0
    while aux <= n :
        valor += aux
        aux+=1
    print(valor)

if __name__ == '__main__':
    main()

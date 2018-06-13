def main():
    n = int(input("insira o numero n"))
    aux = 1
    soma = 0
    while aux <= n :
        soma += int(input("digite 1 numero"))
        aux += 1
    print(soma)
    print(soma/n)

if __name__ == '__main__':
    main()

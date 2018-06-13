def main():
    n = int(input("insira o numero n"))
    aux = 1
    maior = 0
    while aux <= n :
        x = int(input("digite 1 numero"))
        if x > maior :
            maior = x
        aux += 1
    print(maior)

if __name__ == '__main__':
    main()

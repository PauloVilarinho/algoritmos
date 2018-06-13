def main():
    n = int(input("digite o numero n"))

    soma = 0
    for i in range(1,n+1):
        soma += i/(n-(i-1))

    print(soma)


if __name__ == '__main__':
    main()

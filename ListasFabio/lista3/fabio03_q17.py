def main():
    n = int(input("digite o numero n"))

    soma = 0.0
    for i in range(1,n+1):
        soma += 1/i

    print(soma)


if __name__ == '__main__':
    main()

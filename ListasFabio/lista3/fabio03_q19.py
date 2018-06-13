def main():
    n = int(input("digite o numero n"))

    soma = 0
    for i in range(1,n+1):
        x = (n-(i-1))
        if i%2 == 0 :
            soma -= x/i
        else :
            soma += i/x
    print(soma)


if __name__ == '__main__':
    main()

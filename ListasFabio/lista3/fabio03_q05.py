def main():
    inicial = int(input("digite um numero"))
    valor = fatorial(inicial)
    print(valor)


def fatorial(n):
    if n == 0 :
        return 1
    else :
        return n*fatorial(n-1)

if __name__ == '__main__':
    main()

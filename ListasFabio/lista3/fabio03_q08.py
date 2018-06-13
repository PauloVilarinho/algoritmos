def main():
    n = int(input("digite o numero"))
    limite_s = float(input("digite o limite superior"))
    limite_i = float(input("digite o limite inferior"))
    aux = 1
    while (aux*n) <= limite_s :
        valor = aux*n
        aux += 1
        if valor >= limite_i :
            print(valor)

if __name__ == '__main__':
    main()

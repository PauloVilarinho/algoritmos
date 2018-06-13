def main():
    n = int(input('digite o numero de bois'))
    peso_g = 0
    peso_m = 999999
    for i in range(n):
        peso = float(input('digite o peso do boi'))
        if peso >= peso_g :
            peso_g = peso
            index_g = i+1
        elif peso <= peso_m:
            peso_m = peso
            index_m = i+1

    print("boi gordo",index_g,"peso",peso_g)
    print("boi magro",index_m,"peso",peso_m)


if __name__ == '__main__':
    main()

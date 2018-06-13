while True:
    try:
        quantidade = int(input())
        numerador = 0
        denominador = 0
        for i in range(quantidade):
            nota,carga = [int(i) for i in input().split()]
            numerador += nota*carga
            denominador += carga

        ira = numerador/(denominador*100)
        print("{:.4f}".format(ira))

    except:
        break

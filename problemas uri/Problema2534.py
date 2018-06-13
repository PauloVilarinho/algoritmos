while True:
    try:
        pessoas,consultas = [int(i) for i in input().split()]
        lista = []
        for i in range(pessoas):
            lista.append(int(input()))

        lista.sort(reverse=True)

        for i in range(consultas):
            x = int(input())
            print(lista[x-1])



    except:
        break

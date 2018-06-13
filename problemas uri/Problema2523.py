while True:
    try:
        alfabeto = input()
        quantidade = int(input())
        pedido = [int(i) for i in input().split()]
        saida = ''
        for i in pedido:
            saida += alfabeto[i-1]

        print(saida)



    except EOFError:
        break

while True:
    try:
        linhas,colunas = [int(i) for i in input().split()]



        for i in range(linhas):
            vetor = [int(i) for i in input().split()]
            for j in range(colunas):
                if vetor[j] == 2:
                    pikax = i
                    pikay = j
                elif vetor[j] == 1:
                    ashx = i
                    ashy = j

        passos = abs(ashx - pikax) + abs(ashy - pikay)

        print(passos)
    except EOFError:
        break

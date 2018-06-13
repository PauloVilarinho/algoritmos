def main():
    n = int(input('digite o numero de votantes'))
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    nulo = 0
    branco = 0
    for i in range(n):
        voto = int(input("digite o voto"))
        if voto == 1 :
            candidato1 += 1
        elif voto == 2 :
            candidato2 += 1
        elif voto == 3 :
            candidato3 += 1
        elif voto == 9 :
            nulo += 1
        elif voto == 0 :
            branco += 1

    if candidato1 > candidato2 :
        if candidato1 > candidato3:
            vencedor = "candidato 1 venceu"
        elif candidato1 < candidato3:
            vencedor = 'candidato 3 venceu'
        else :
            vencedor = 'empate entre candidato 1 e candidato 3'
    elif candidato1 < candidato2 :
        if candidato2 > candidato3:
            vencedor = "candidato 2 venceu"
        elif candidato2 < candidato3:
            vencedor = 'candidato 3 venceu'
        else :
            vencedor = 'empate entre candidato 2 e candidato 3'
    else :
        vencedor = "empate entre candidato 2 e candidato 1"

    print("candidato 1",candidato1,"candidato 2",candidato2,'candidato3',candidato3)
    print("votos nulos", nulo)
    print("votos brancos", branco)
    print(vencedor)


if __name__ == '__main__':
    main()

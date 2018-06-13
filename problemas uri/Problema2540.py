while True:
    try:
        quantidade = int(input())
        votos = [int(i) for i in input().split()]
        afavor = 0
        for i in votos:
            if i == 1 :
                afavor += 1

        if afavor >= (2*quantidade)/3 :
            print("impeachment")
        else:
            print("acusacao arquivada")


    except:
        break

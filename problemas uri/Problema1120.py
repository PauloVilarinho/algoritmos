erro,valor = [i for i in input().split()]

while erro != "0" or valor != "0" :
    aux = []
    for digito in valor :
        if digito != erro :
            aux.append(digito)

    if aux != [] :
        print(int("".join(aux)))
    else :
        print("0")

    erro,valor = [i for i in input().split()]

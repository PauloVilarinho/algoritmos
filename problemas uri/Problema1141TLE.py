quantity = int(input())
while quantity != 0 :
    test = []
    for j in range(quantity):
        test.append(input())

    test.sort(key= lambda s : len(s) , reverse=False)
    maior = 0
    for i in test:
        menor = i
        valor = 0
        for k in test:
            if menor in k :
                valor += 1
                menor = k
        if maior < valor :
            maior = valor

    print(maior)

    quantity = int(input())

quantity = int(input())

numeros = [0] * 2001
for i in range(quantity):
    entrada = int(input())
    numeros[entrada] += 1

for i in range(len(numeros)):
    if numeros[i] != 0 :
        print("%d aparece %d vez(es)" %(i,numeros[i]))

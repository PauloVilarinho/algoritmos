quantity = int(input())
lista = input().split()
multiplos2 = 0
multiplos3 = 0
multiplos4 = 0
multiplos5 = 0
for i in range (quantity) :
	lista[i] = int(lista[i])

for i in (lista) :
	if i%2 == 0 :
		multiplos2 += 1
	if i%3 == 0 :
		multiplos3 += 1
	if i%4 == 0 :
		multiplos4 += 1
	if i%5 == 0 :
		multiplos5 += 1

print("%d Multiplo(s) de 2" %multiplos2)
print("%d Multiplo(s) de 3" %multiplos3)
print("%d Multiplo(s) de 4" %multiplos4)
print("%d Multiplo(s) de 5" %multiplos5)

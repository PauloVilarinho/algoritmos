lista = input().split()

while lista[0] != "0" :
	ladoa, ladob, percentagem = [int(i) for i in lista]
	area_necessaria = ladoa*ladob
	area_total = (area_necessaria*100)/percentagem
	ladoc = int(area_total**(1/2))
	print(ladoc)
	lista = input().split()
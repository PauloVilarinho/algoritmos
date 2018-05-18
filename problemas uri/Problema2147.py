quantity = int(input())

for i in range(quantity) :
	palavra = input()
	tamanho = palavra.__len__()
	tempo = tamanho*0.01
	print("{:.2f}" .format(tempo))
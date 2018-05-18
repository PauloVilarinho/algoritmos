abas, quantidade = [int(i) for i in input().split()]
for i in range (quantidade) :
	acao = input().strip()
	if acao == "fechou" :
			abas += 1
	if acao == "clicou" :
			abas -= 1

print(abas)
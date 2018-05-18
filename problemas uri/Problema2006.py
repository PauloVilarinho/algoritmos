tipo = input()
resposta = input().split()
total = 0

for i in resposta :
	if i == tipo :
		total += 1
print(total)
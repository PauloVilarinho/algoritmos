linhas,colunas, branco = [int(i) for i in input().split()]

while linhas != 0 or colunas != 0 or branco != 0 :
	total = 0
	if linhas%2 == 0 and colunas%2 == 0 :
		total = ((linhas - 7)*(colunas-7)//2 ) + branco
	else :
		total = ((linhas - 7)*(colunas-7)//2 )
	print(total)
	linhas,colunas, branco = [int(i) for i in input().split()]
	
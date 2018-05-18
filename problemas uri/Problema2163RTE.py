linhas,colunas = [int(i) for i in input().split()]

vetor = []
sabre = False

for i in range (linhas):
	entrada = input().split()
	vetor.append(entrada)
	
for i in range (1,linhas-1):
	if sabre :
		break
	for j in range (1,colunas-1):
		if not("42" in vetor[i]) :
			break
		else:
			if vetor[i][j] == "42" :
				if vetor [i+1][j] == "7" :
					if vetor [i+1][j+1] == "7" :
						if vetor [i+1][j-1] == "7" :
							if vetor [i][j+1] == "7" :
								if vetor [i][j-1] == "7" :
									if vetor [i-1][j+1] == "7" :
										if vetor [i-1][j] == "7" :
											if vetor [i-1][j-1] == "7" :
												sabre = True
												sabrex = i+1
												sabrey = j+1
												break

if sabre:
	print(sabrex,sabrey)
else :
	print(0,0)





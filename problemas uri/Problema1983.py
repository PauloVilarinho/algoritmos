quantity = int(input())

aluno = 0
nota  =  0.0

for i in range(quantity) :
	entrada = input()
	matricula = int(entrada.split()[0])
	media = float(entrada.split()[1])
	if media > nota :
		nota = media
		aluno = matricula
if nota >= 8 :
	print(aluno)
else :
	print("Minimum note not reached")

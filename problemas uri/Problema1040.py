Notas = input()

Nota1 = float(Notas.split()[0])
Nota2 = float(Notas.split()[1])
Nota3 = float(Notas.split()[2])
Nota4 = float(Notas.split()[3])

media = ((Nota1*2)+(Nota2*3)+(Nota3*4)+(Nota4*1))/10

if (media>=7):
	print("Media: {:.1f}".format(media))
	print("Aluno aprovado.")
elif (media<5):
	print("Media: {:.1f}".format(media))
	print("Aluno reprovado.")
else:
	print("Media: {:.1f}".format(media))
	print("Aluno em exame.")
	exame = float(input())
	print("Nota do exame: {:.1f}".format(exame))
	mediafinal = (media+exame)/2
	if (mediafinal>=5):
		print ("Aluno aprovado.")
		print ("Media final: {:.1f}".format(mediafinal))
	else:
		print ("Aluno reprovado.")
		print ("Media final: {:.1f}".format(mediafinal))
altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))

imc = peso/(altura**2)

print("Imc = %.2f" %imc)

if imc > 40 :
	print("paciente possui obesidade grau 3! porfavor tomar as providencias!")
else :
	print("ta de boas pode comer seu biscoito negresco!")

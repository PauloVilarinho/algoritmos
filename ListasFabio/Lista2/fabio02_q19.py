"""
	Questão: Lista 2 19
	Descrição: calcula imc e retorna categoria de risco
"""

def main():
	#entrada
	altura = float(input("digite a altura em metros: "))
	peso = float(input("digite seu peso em kilogramas: "))
	#processamento
	imc = peso/(altura**2)
	if imc>30 :
		texto = "obesidade morbida"
	elif 25<imc<=30 :
		texto = "obesidade"
	else :
		texto = "peso normal"
 	#saida
	print("O seu imc é :%.2f . Você está com %s" %(imc,texto))

if __name__ == '__main__':
	main()
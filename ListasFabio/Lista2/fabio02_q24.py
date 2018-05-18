"""
	Questão: Lista 2 24
	Descrição: calcula as raizes da equação do segundo grau
"""

def main():
	#entrada
	a = float(input("digite o valor A da equação: "))
	b = float(input("digite o valor B da equação: "))
	c = float(input("digite o valor C da equação: "))
	#processamento
	delta = b**2 - 4*a*c
	if delta > 0 :
		x1 = ((-b) + delta**(1/2))/(2*a)
		x2 = ((-b) - delta**(1/2))/(2*a)
	elif delta == 0 :
		x1 = -b/(2*a)

	#saida
	if delta > 0 :
		print("as raizes da equação são %.2f %.2f" %(x1,x2))
	elif delta == 0 :
		print("a raiz da equação é %d" %x1)
	else :
		print("a equação não possui raiz")

if __name__ == '__main__':
	main()

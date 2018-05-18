'''
	Questão Lista 1 43
	Descrição resolve um sistema linear de duas equações
'''

def main():
	#entrada
	a,b,c,d,e,f = [float(i) for i in input("digite os valores de a, b, c, d, e, f :").split()]
	#processamento
	possivel = False
	if (a*e - b*d) != 0 :
		x = (c*e - b*f)/(a*e - b*d)
		y = (a*f - c*d)/(a*e - b*d)
		possivel = True
	#saida
	if possivel :
		print("o valor de x é %.2f e o de y é %.2f" %(x,y))
	else :
		print("Impossivel de achar um valor de x e y")

if __name__ == '__main__':
	main()
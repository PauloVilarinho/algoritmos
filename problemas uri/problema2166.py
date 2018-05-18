entrada = int(input())

valor = [0,1/2]

for i in range (2,101) :
	valor.append(1/(2+valor[i-1]))

print("%.10f" %(1+valor[entrada]))
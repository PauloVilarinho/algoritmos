saida,tempo,fuso = [int(i) for i in input().split()]

esperado = saida + tempo + fuso

if esperado > 24 :
	esperado = esperado - 24
elif esperado < 0 :
	esperado = 24 + esperado

print(esperado)
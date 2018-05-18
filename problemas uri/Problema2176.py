entrada = input()
lista = list(entrada)
quantidade = 0
for i in lista :
	if i == "1":
		quantidade += 1

if quantidade%2 == 0 :
	print(entrada+"0")
else:
	print(entrada+"1")
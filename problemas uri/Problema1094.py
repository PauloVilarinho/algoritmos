x = int(input())
total = 0
totalrato = 0
totalsapo = 0
totalcoelho = 0


for i in range(x):
	entrada = input()
	quantity = int(entrada.split()[0])
	tipo = entrada.split()[1]
	if tipo == "C":
		totalcoelho = totalcoelho + quantity
	elif tipo == "S":
		totalsapo = totalsapo + quantity
	elif tipo == "R":
		totalrato = totalrato + quantity
	total = total + quantity

print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %totalcoelho)
print("Total de ratos: %d" %totalrato)
print("Total de sapos: %d" %totalsapo)
totalcoelho = (totalcoelho/total)*100
totalrato = (totalrato/total)*100
totalsapo = (totalsapo/total)*100
print("Percentual de coelhos: {:.2f} %".format(totalcoelho))
print("Percentual de ratos: {:.2f} %".format(totalrato))
print("Percentual de sapos: {:.2f} %".format(totalsapo))

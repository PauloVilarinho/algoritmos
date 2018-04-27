Numbers = input()

A = float(Numbers.split()[0])
B = float(Numbers.split()[1])
C = float(Numbers.split()[2])

delta = ((B**2) - 4*A*C)
if (A != 0):
	if (delta >= 0):
		R1 = ((-B)+(delta**(1/2)))/(2*A)
		R2 = ((-B)-(delta**(1/2)))/(2*A)

		print ("R1 = {:.5f}".format(R1))
		print ("R2 = {:.5f}".format(R2))
	else:
		print("Impossivel calcular")
else:
	print("Impossivel calcular")		
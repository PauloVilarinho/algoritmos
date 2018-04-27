salario = float(input())

if (0.00<=salario<=2000.00):
	tax = 0
	fix = 0
	piso = 0
elif (2000.00<salario<=3000.00):
	tax = 8
	fix = 0
	piso = 2000.00
elif (3000.00<salario<=4500.00):
	tax = 18
	fix = 80.00
	piso = 3000.00
elif (4500.00<salario):
	tax = 28
	fix = 350.00
	piso = 4500.00

if tax == 0 :
	print("Isento")
else: 
	imposto = fix+ ((salario - piso)*(tax*0.01))
	print ("R$ {:.2f}".format(imposto))

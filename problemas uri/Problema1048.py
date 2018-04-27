oldsalary = float(input())
if (0.00 <= oldsalary <= 400.00):
	percentage = 15
elif (400.00 < oldsalary <= 800.00):
	percentage = 12
elif (800.00 < oldsalary <= 1200.00):
	percentage = 10
elif (1200.00 < oldsalary <= 2000.00):
	percentage = 7
elif (2000.00 < oldsalary ):
	percentage = 4
	



wageup = oldsalary*(0.01*percentage)
newsalary = oldsalary + wageup


print ("Novo salario: {:.2f}".format(newsalary))
print ("Reajuste ganho: {:.2f}".format(wageup))
print ("Em percentual: {0} %".format(percentage))


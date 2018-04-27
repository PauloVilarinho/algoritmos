name = input()
salary = float(input())
vendas = float(input())

bonus = vendas*0.15

salaryreal= salary + bonus

print ("TOTAL = R$ {:.2f}".format(salaryreal))

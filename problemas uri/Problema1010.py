product1 = input()
product2 = input()

code1 = int(product1.split()[0])
quantity1 = int(product1.split()[1])
price1 = float(product1.split()[2])
code2 = int(product2.split()[0])
quantity2 = int(product2.split()[1])
price2 = float(product2.split()[2])

pricetotal= (quantity1*price1)+(quantity2*price2)

print('VALOR A PAGAR: R$ {:.2f}'.format(pricetotal))
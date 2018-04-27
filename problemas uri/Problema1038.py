Numbers = input()

code = str(Numbers.split()[0])
quantity = int(Numbers.split()[1])

Codes = {
	    "1":4.00,
	    "2":4.50,
	    "3":5.00,
	    "4":2.00,
	    "5":1.50,	
}

value = (Codes.get(code))*quantity

print("Total: R$ {:.2f}".format(value))
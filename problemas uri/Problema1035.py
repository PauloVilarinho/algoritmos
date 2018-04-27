Numbers = input()

A = int(Numbers.split()[0])
B = int(Numbers.split()[1])
C = int(Numbers.split()[2])
D = int(Numbers.split()[3])

bool1 = bool2 = bool3 = bool4 = bool5 = False

if (B>C):
	bool1 = True
else:
	bool1 = False


if (D>A):
	bool2 = True
else:
	bool2 = False
	
if ((C+D)>(A+B)):
	bool3 = True
else:
	bool3 = False


if ((C>0) and (D>0)):
	bool4 = True
else:
	bool4 = False


if ((A%2)==0):
	bool5 = True
else:
	bool5 = False

if(bool1 and bool2 and bool3 and bool4 and bool5):
	print ("Valores aceitos")
else:
	print("Valores nao aceitos")


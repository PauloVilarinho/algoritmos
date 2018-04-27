a,b,c = [float(i) for i in input().split()]

if (abs(b-c)<a<(b+c)):
	bool1 = True
else:
	bool1 = False

if (abs(a-c)<b<(a+c)):
	bool2 = True
else:
	bool2 = False

if (abs(a-b)<c<(a+b)):
	bool3 = True
else:
	bool3 = False


if (bool1 and bool2 and bool3):
	perimetro = a+b+c
	print("Perimetro = {:.1f}".format(perimetro))
else:
	area = ((a+b)/2)*c
	print("Area = {:.1f}".format(area))	
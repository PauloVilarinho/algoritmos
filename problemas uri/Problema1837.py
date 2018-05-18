import math

a,b = [int(i) for i in input().split()]

if a>0  and b<0 :
	quociente = int(a/b)
elif a<0 and b>0 :
	quociente = a//b
elif a<0 and b<0 :
	quociente = math.ceil(a/b)
else:
	quociente = a//b

resto = a - (b*quociente)

print(quociente,resto)
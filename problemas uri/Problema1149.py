lista =  input().split()
a = int(lista[0])
b = int(lista[1])
x = 2

while b<= 0 :
	b = int( lista[x])
	x += 1

total = 0

for i in range (b):
	total += a
	a += 1
print(total)

quantity = int(input())
i = 0
f = [0 , 1]
while len(f) < 70 :
	novoindice = [f[i] + f[i+1]]
	f = f + novoindice
	i += 1 
for z in range (quantity):
	x = int(input())
	print("Fib(%d) = %d" %(x,f[x]))
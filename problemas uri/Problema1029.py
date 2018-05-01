quantity = int(input())
i = 0 
fib1 = [0, 1]
fib2 = [0, 0]
while len(fib1)<=39 :
	novoindice1 = [fib1[i]+fib1[i+1]]
	fib1 = fib1 + novoindice1
	novoindice2 = [fib2[i]+fib2[i+1] + 2]
	fib2 = fib2 + novoindice2
	i += 1

for i in range(quantity) :
	x = int(input())
	print("fib(%d) = %d calls = %d" %(x,fib2[x],fib1[x]))
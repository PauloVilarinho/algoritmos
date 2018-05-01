X = int(input())
i = 0
f = [0 , 1]
while len(f) < X :
	novoindice = [f[i] + f[i+1]]
	f = f + novoindice
	i += 1 

for z in range (len(f)):
	if z+1 != len(f):
		print(f[z], end=" ")
	else:
		print(f[z])



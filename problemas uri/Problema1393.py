lajotas = int(input())

f = [0, 1]
i = 0
while len(f) < 45 :
	it = f[i] + f[i+1]
	f.append(it)
	i += 1

while lajotas != 0 :
	print(f[lajotas+1])
	lajotas = int(input())
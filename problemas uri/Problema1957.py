def inttohex(n):

	x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
	result = []
	while n>0 :
		result.append(x16[(n%16)])
		n = n//16
	result.reverse()
	return (''.join(result))

print(inttohex(int(input())))
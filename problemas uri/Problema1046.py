i, e = [int(i) for i in input().split()]

if i>=e :
	h = (24 - i + e)
else:
	h = e-i

print ("O JOGO DUROU %d HORA(S)" %h)

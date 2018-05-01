pa = []
ipa = []
for i in range (15):
	x = int(input())
	if x%2 == 0 :
		pa.append(x)
		if len(pa) == 5 :
			for i in range (len(pa)):
				print("par[%d] = %d" %(i,pa[i]))
			pa = []
	if x%2 != 0 :
		ipa.append(x)
		if len(ipa) == 5 :
			for i in range (len(ipa)):
				print("impar[%d] = %d" %(i,ipa[i]))
			ipa = []

for i in range (len(ipa)):
	print("impar[%d] = %d" %(i,ipa[i]))
for i in range (len(pa)):
	print("par[%d] = %d" %(i,pa[i]))
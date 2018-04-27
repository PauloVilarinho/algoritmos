
I = 0.0
while I <= 2 :
	if int(I) == I:
		print("I=%d J=%d" %(I,1+I))
		print("I=%d J=%d" %(I,2+I))
		print("I=%d J=%d" %(I,3+I))
	else:
		print("I=%.1f J=%.1f" %(I,1+I))
		print("I=%.1f J=%.1f" %(I,2+I))
		print("I=%.1f J=%.1f" %(I,3+I))
	
	I = I + 0.2
	if 1.8<I<2 : 
		I=2
	
	

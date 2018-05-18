a,b,c = [int(i) for i in input().split()]

if a == b or a == c or b == c :
	print("S")
elif (a + b) == c or (a + c) == b or (c + b) == a :
	print("S")
else :
	print("N")
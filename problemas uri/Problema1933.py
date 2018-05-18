a,b =[int(i) for i in input().split()]
maior = (a+b+abs(a-b))//2
if a==b :
	print(a)
else :
	print(maior)
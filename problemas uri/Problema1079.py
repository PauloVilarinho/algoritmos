quantity = int(input())

for i in range(quantity):
	a,b,c = [float(x) for x in input().split()]
	media = ((a*2)+(b*3)+(c*5))/10
	print("{:.1f}".format(media))
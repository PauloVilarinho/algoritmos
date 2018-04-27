positivos = 0
total = 0
for x in range(6):
	y = float(input())
	if y>0 :
		positivos = positivos + 1
		total = total + y
media = total/positivos
print(positivos,"valores positivos")
print("{:.1f}".format(media))
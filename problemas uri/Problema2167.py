quantidade = int(input())

entrada = input().split()
index = 0
for i in range(1,len(entrada)) :
	if int(entrada[i]) < int(entrada[i-1]) :
		index = i + 1
		break
print(index)

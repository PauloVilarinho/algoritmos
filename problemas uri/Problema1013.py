Numbers = input()

A = int(Numbers.split()[0])
B = int(Numbers.split()[1])
C = int(Numbers.split()[2])

MaiorAB = int((A + B + abs(A - B))/2)

MaiorABC = int((MaiorAB + C + abs(MaiorAB - C))/2)

print(MaiorABC, "eh o maior")

antiga,nova = [float(i) for i in input().split()]


percentual = ((nova - antiga)/antiga)*100

print("{:.2f}%".format(percentual))

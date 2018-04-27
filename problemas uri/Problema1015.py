ponto1 = input()
ponto2 = input()

x1 = float(ponto1.split()[0])
y1 = float(ponto1.split()[1])
x2 = float(ponto2.split()[0])
y2 = float(ponto2.split()[1])

distance = ((((x2-x1)**2)+((y2-y1)**2))**(1/2))

print ("{:.4f}".format(distance))
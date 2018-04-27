Numbers = input()

A = float(Numbers.split()[0])
B = float(Numbers.split()[1])
C = float(Numbers.split()[2])


ATriangle = (A*C)/2
ACircle =  3.14159*(C**2)
ATrapezium = ((A+B)/2)*C
ASquare = B**2
ARectangle = A*B

print("TRIANGULO: {:.3f}".format(ATriangle))
print("CIRCULO: {:.3f}".format(ACircle))
print("TRAPEZIO: {:.3f}".format(ATrapezium))
print("QUADRADO: {:.3f}".format(ASquare))
print("RETANGULO: {:.3f}".format(ARectangle))

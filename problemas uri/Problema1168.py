letras = [6,2,5,5,4,5,6,3,7,6]

quantity = int(input())

for i in range(quantity):
    leds = 0
    display = input()
    for j in display :
        leds += letras[int(j)]
    print("%d leds" %leds)

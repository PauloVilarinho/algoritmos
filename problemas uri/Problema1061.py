diainicio = input()
horarioinicio = input()
diafinal = input()
horariofinal = input()

dia1 = int(diainicio.split()[1])
dia2 = int(diafinal.split()[1])
hora1,min1,seg1 = [int(i) for i in horarioinicio.split(':')]
hora2,min2,seg2 = [int(i) for i in horariofinal.split(':')]

tempo1 = dia1*86400 + hora1*3600 + min1*60 + seg1
tempo2 = dia2*86400 + hora2*3600 + min2*60 + seg2

tempototal = tempo2 - tempo1

diatotal = int(tempototal/86400)
tempototal = tempototal - diatotal*86400

horatotal = int(tempototal/3600)
tempototal = tempototal - horatotal*3600

mintotal = int(tempototal/60)
tempototal = tempototal - mintotal*60

segtotal = tempototal

print(diatotal, "dia(s)")
print(horatotal, "hora(s)")
print(mintotal, "minuto(s)")
print(segtotal, "segundo(s)")
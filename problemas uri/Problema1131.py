cal = 1 
vg = 0
vi = 0
em = 0
total = 0

while cal == 1 :
	gi,gg = [int(i) for i in input().split()]
	if gi>gg :
		vi = vi + 1
	elif gg>gi :
		vg = vg + 1
	elif gg==gi:
		em = em + 1
	total = total + 1
	cal= int(input("Novo grenal (1-sim 2-nao)\n")) 
print("%d grenais" %total)
print ("Inter:%d" %vi)
print ("Gremio:%d" %vg)
print ("Empates:%d" %em)
if vg > vi:
	print("Gremio venceu mais")
elif vi > vg:
	print("Inter venceu mais")
else:
	print("Nao houve vencedor")


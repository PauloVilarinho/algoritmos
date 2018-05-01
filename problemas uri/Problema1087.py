ii = 1
ji = 1
ie = 1
je = 1

while ii != 0 and ji != 0 and ie != 0 and je != 0 :
	ii,	ji, ie, je = [int(i) for i in input().split()]
	if (ii != 0 and ji != 0 and ie != 0 and je != 0):
		if ii == ie and ji == je :
			print(0)
		elif ii == ie or ji == je or ii+ji == ie +je or  ii - ji == ie -je :
			print(1)
		else:
			print(2)
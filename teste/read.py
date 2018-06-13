file = open("read.txt","r+")

file.write("mais uma linha pq eu posso\n")

f = file.readlines()
for i in f:
    print(i)

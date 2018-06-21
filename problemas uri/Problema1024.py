quantity = int(input())

for i in range(quantity):
    texto = input()
    aux1 = []
    for char in texto :
        valor = ord(char)
        if char.isalpha():
            valor += 3
        aux1.append(chr(valor))
    texto = "".join(aux1)
    texto = texto[::-1]
    aux2 = []
    for i in range(len(texto)) :
        valor = ord(texto[i])
        if i >= int(len(texto)/2):
            valor -= 1
        aux2.append(chr(valor))
    texto = "".join(aux2)
    print(texto)

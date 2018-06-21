def main():
    frase = input('digite uma frase: ')

    nova_frase = ""

    for i in range(len(frase)):
        if frase[i] == '0':
            nova_frase += 'zero'
        elif frase[i] == '1' :
            nova_frase += 'um'
        elif frase[i] == '2' :
            nova_frase += 'dois'
        elif frase[i] == '3' :
            nova_frase += 'tres'
        elif frase[i] == '4' :
            nova_frase += 'quatro'
        elif frase[i] == '5' :
            nova_frase += 'cinco'
        elif frase[i] == '6' :
            nova_frase += 'seis'
        elif frase[i] == '7' :
            nova_frase += 'sete'
        elif frase[i] == '8' :
            nova_frase += 'oito'
        elif frase[i] == '9' :
            nova_frase += 'nove'
        else :
            nova_frase += frase[i]

    print(nova_frase)




if __name__ == '__main__':
    main()

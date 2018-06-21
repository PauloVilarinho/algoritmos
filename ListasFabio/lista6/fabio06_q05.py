def main():
    data = input()

    data_lista = data.split('/')
    numero_mes = int(data_lista[1])

    if numero_mes == 1 :
        mes = "janeiro"
    elif numero_mes == 2 :
        mes = 'fevereiro'
    elif numero_mes == 3 :
        mes = 'março'
    elif numero_mes == 4 :
        mes = 'abril'
    elif numero_mes == 5 :
        mes = 'maio'
    elif numero_mes == 6 :
        mes = 'junho'
    elif numero_mes == 7 :
        mes = 'julho'
    elif numero_mes == 8 :
        mes = 'agosto'
    elif numero_mes == 9 :
        mes = 'setembro'
    elif numero_mes == 10 :
        mes = 'outubro'
    elif numero_mes == 11 :
        mes = 'novembro'
    elif numero_mes == 12 :
        mes = 'dezembro'


    print(data_lista[0],"de", mes ," de",data_lista[2])

if __name__ == '__main__':
    main()

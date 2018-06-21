def main():
    horario = input()

    horario_lista = horario.split(':')


    print(horario_lista[0],"hora(s),", horario_lista[1] ,"minuto(s),",horario_lista[2],"segundo(s)")

if __name__ == '__main__':
    main()

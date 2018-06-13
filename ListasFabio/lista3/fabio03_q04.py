def main():
    inicial = float(input("digite o numero inicial"))
    razao = float(input("digite a razão"))
    limite = float(input("digite o valor limite"))
    while inicial <= limite :
        print(inicial)
        inicial *= razao


if __name__ == '__main__':
    main()

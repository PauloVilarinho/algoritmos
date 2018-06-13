def main():
    n = int(input('digite o numero de habitantes'))
    soma_s = 0
    soma_f = 0
    soma_ps = 0
    for i in range(n):
        salario = float(input('digite o salario'))
        filhos = int(input('digite a quantidade de filhos'))
        soma_s += salario
        soma_f += filhos
        if salario <= 1000 :
            soma_ps += 1

    print(soma_s/n)
    print(soma_f/n)
    print((soma_ps/n)*100)

if __name__ == '__main__':
    main()

"""
	Questão: Lista 2b 07
	Descrição: receba o salario do trabalhador e retorna o aumento salarial
"""

def main():
    #entrada
    salario = float(input("digite o seu salario: "))
    #processamento
    if salario <= 280 :
        aumento = 20
    elif salario <= 700 :
        aumento = 15
    elif salario <= 1500 :
        aumento = 10
    else :
        aumento = 5
    #saida
    print("salario anterior = %.2f" %salario)
    print("percentual aumentado = %d %%" %aumento)
    print("valor do aumento = %.2f" %(salario*(aumento/100)))
    print("novo salario = %.2f" %(salario*(1+(aumento/100))))

if __name__ == '__main__':
    main()

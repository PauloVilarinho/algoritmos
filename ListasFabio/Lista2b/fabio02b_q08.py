"""
	Questão: Lista 2b 08
	Descrição: receba o salario do trabalhador e retorna o aumento salarial
"""

def main():
    #entrada
    hora = float(input("digite o valor da sua hora: "))
    #processamento
    salario = hora*220
    if salario <= 900 :
        desconto = 0
    elif salario <= 1500 :
        desconto = 5
    elif salario <= 2500 :
        desconto = 10
    else :
        desconto = 20

    x = 0.1 + (desconto/100)
    #saida
    print("salario anterior = %.2f \n IR = %d %% \n INSS = %.2f \n FGTS = %.2f \n total dos descontos = %.2f \n Salario liquido = %.2f" %(salario, salario*(desconto/100),salario*0.1,salario*0.11,salario*x,salario*(1-x) ))

if __name__ == '__main__':
    main()

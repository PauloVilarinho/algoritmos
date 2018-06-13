"""
	Questão: Lista 2b 0
	Descrição: receba 2 notas e retorna se foi aprovado ou não
"""

def main():
    #entrada
    nota1 = float(input("digite nota 1: "))
    nota2 = float(input("digite nota 2: "))
    #processamento
    media = (nota1+nota2)/2
    #saida
    if media == 10 :
        print("Aprovado com Distinção")
    elif media >= 7 :
        print("Aprovado")
    else :
        print("Reprovado")

if __name__ == '__main__':
    main()

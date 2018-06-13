"""
	Questão: Lista 2b 10
	Descrição: retorna aprovação
"""

def main():
    #entrada
    nota1 = int(input("digite nota 1: "))
    nota2 = int(input("digite nota 2: "))
    #processamento
    media = (nota1 + nota2)/2
    #saida
    if media >= 6 :
        print("Aprovado")
    else :
        print("Reprovado")

if __name__ == '__main__':
    main()

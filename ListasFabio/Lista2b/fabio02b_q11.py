"""
	Questão: Lista 2b 11
	Descrição: retorna uma as centenas dezenas e unidades
"""

def main():
    #entrada
    numero = int(input("digite um numero menos que 1000: "))
    #processamento
    centenas = numero//100
    dezenas = (numero%100)//10
    unidade = (numero%100)%10

    if centenas == 0 :
        tcentenas = ""
    else :
        tcentenas = "%d centenas " %centenas
    #saida
    print("%s%d dezenas %d unidades " %(tcentenas,dezenas,unidade))
if __name__ == '__main__':
    main()

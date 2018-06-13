"""
	Questão: Lista 2b 13
	Descrição: retorna se o numero é decimal ou inteiro
"""

def main():
    #entrada
    perg1 = input("telefonou para a vitima?(s/n)")
    perg2 = input("esteve no local do crime?(s/n)")
    perg3 = input("mora perto da vitima?(s/n)")
    perg4 = input("devia para a vitima?(s/n)")
    perg5 = input("ja trabalhou com a vitima?(s/n)")
    #processamento
    total = 0
    if perg1 == "s" :
        total += 1
    if perg2 == "s" :
        total += 1
    if perg3 == "s" :
        total += 1
    if perg4 == "s" :
        total += 1
    if perg5 == "s" :
        total += 1
    if total == 5 :
        print("Assasino")
    elif 3<=total<=4 :
        print("Cúmplice")
    elif total == 2 :
        print("Suspeito")
    else :
        print("Inocente")
    #saida

if __name__ == '__main__':
    main()

def main():
    verbo = input()
    prefixo = verbo[:-2]

    print("Eu", prefixo + 'o')
    print("Tu", prefixo + 'es')
    print("Ele", prefixo + 'e')
    print("Nós", prefixo + 'emos')
    print("Vós", prefixo + 'eis')
    print("Eles", prefixo + 'evem')


if __name__ == '__main__':
    main()

def main():
    frase = input("digite uma frase")
    nova_frase = ""
    for letra in frase:
        nova_frase += letra*2

    print(nova_frase)

if __name__ == '__main__':
    main()

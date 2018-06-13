def main():
    numero =  int(input("insira um numero inteiro:"))
    while numero != 0 :
        for i in range(1, numero+1) :
            if numero%i == 0 :
                print(i)
        numero =  int(input("insira um numero inteiro:"))

if __name__ == '__main__':
    main()

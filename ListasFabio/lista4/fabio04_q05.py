def main():
    X = int(input("digite o numero X: "))
    N = int(input("digite o numero N: "))

    while N>=2 :
        X = X/N
        N -= 1
        print(X)

if __name__ == '__main__':
    main()

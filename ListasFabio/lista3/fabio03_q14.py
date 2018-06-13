def main():
    n = int(input("insira o numero n"))
    while n**(1/2) != int(n**(1/2)) :
        n -= 1

    print(n)

if __name__ == '__main__':
    main()

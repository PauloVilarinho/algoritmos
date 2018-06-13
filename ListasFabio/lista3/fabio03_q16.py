def main():
    n = int(input("digite o numero n"))
    fib = [0,1]
    for i in range(n-2) :
        fib.append(fib[i] + fib[i+1])

    print(fib)


if __name__ == '__main__':
    main()

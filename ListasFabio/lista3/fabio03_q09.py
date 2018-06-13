def main():
    limite_s = float(input("digite o limite superior"))
    limite_i = float(input("digite o limite inferior"))
    while limite_i <= limite_s :
        if limite_i%2 == 0 :
            print(limite_i)
        limite_i += 1

if __name__ == '__main__':
    main()

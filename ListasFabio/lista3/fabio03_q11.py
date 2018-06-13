def main():
    limite_s = float(input("digite o limite superior"))
    limite_i = float(input("digite o limite inferior"))
    while limite_i <= limite_s :
        if is_prime(limite_i) :
            print(limite_i)
        limite_i += 1


def is_prime(x):
    if x == 1 or x == 2 :
        return True
    else :
        aux = 2
        while aux <= x**(1/2) :
            if x%aux == 0 :
                return False
            aux += str1
        return True

if __name__ == '__main__':
    main()

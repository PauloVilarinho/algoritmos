def main():
    x = input()
    print("é palindroma") if x == x[::-1] else print("não é palindroma")


if __name__ == '__main__':
    main()

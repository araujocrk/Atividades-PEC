def main():
    for num in range(10, 1001, 10):
        if num != 1000:
            print(num, end=', ')
        else:
            print(num, end='.')

if __name__ == '__main__':
    main()
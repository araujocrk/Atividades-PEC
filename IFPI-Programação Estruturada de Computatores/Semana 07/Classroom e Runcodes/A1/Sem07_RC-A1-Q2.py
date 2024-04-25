def eh_impar(n):
    return n % 2 == 1


def main():
    numero = int(input().strip())

    print(f'{eh_impar(numero)}')

if __name__ == '__main__':
     main()
def eh_impar(n):
    return n % 2 == 1


def main():
    numero = int(input('Digite um número para saber se é ímpar: '))

    print(f'{numero} é ímpar? {eh_impar(numero)}')

if __name__ == '__main__':
     main()
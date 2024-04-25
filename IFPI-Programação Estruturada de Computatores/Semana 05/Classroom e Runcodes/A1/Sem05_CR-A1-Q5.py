def reverter(num):
    a = num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    c = num % 10
    num = num // 10
    d = num % 10
    num_invertido = (a * 1000) + (b * 100) + (c * 10) + d
    return  num_invertido

def main():

    numero = int(input('Digite um número entre 1000 e 9999: '))

    reverso = reverter(numero)

    print(f'O reverso desse número é {reverso}')

if __name__ == '__main__':
     main()
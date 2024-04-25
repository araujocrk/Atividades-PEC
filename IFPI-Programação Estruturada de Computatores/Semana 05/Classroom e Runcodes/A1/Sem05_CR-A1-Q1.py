def calcular(a, b, c):
    return 2 * a + 5 * b - c

def main():
    a = int(input('Digite um número para a: '))
    b = int(input('Digite um número para b: '))
    c = int(input('Digite um número para c: '))

    calculo = calcular(a, b, c)

    print(f'O resultado do cálculo é {calculo}')
if __name__ == '__main__':
     main()
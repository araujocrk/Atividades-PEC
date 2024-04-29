def arredondar(dinheiro):
    return round(dinheiro, ndigits = None)

def main():
    dinheiro = float(input('Insira a quantidade de dinheiro: '))

    print(f'O valor mais próximo para se arredondar é R${arredondar(dinheiro)}')

if __name__ == '__main__':
     main()
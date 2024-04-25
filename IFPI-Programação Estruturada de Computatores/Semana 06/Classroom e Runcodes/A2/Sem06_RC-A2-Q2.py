def arredondar(dinheiro):
    return round(dinheiro, ndigits = None)

def main():
    dinheiro = float(input().strip())

    print(f'{arredondar(dinheiro)}')

if __name__ == '__main__':
     main()
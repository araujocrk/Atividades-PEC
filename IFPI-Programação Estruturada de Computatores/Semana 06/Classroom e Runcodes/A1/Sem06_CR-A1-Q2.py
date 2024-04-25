def ordinal(caractere):
    return ord(caractere)

def main():
    caractere = input('Digite um caractere: ')

    print(f'O seu caractere tem como código numérico o {ordinal(caractere)}!')

if __name__ == '__main__':
     main()
     

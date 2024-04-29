def letra(caractere):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ'
    return caractere in letras

def main():
    caractere = input().strip()

    p_letra = letra(caractere)

    print(f'{p_letra}')

if __name__ == '__main__':
     main()
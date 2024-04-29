def consoante(caractere):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ'
    return caractere in consoantes

def main():
    caractere = input().strip()

    fun_consoante = consoante(caractere)

    print(f'{fun_consoante}')

if __name__ == '__main__':
     main()
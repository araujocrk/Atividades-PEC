def consoante(caractere):
    CONSOANTES = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ'
    return caractere in CONSOANTES #Retorna na função se o caractere digitado pelo usuário está na constante CONSOANTES, (Sim = True) (Não = False)

def main():
    caractere = input('Escreva um caractere e veja se ele é uma consoante: ')

    fun_consoante = consoante(caractere)

    print(f'{fun_consoante}')

if __name__ == '__main__':
     main()
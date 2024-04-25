def simbolo(caractere):
    LETRA_NUM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ0123456789'
    return caractere not in LETRA_NUM #Retorna na função se o caractere digitado pelo usuário não está na constante LETRA_NUM, (Sim = True) (Não = False)

def main():
    caractere = input('Escreva um caractere e veja se ele é um símbolo: ')

    fun_simbolos = simbolo(caractere)

    print(f'{fun_simbolos}')

if __name__ == '__main__':
     main()
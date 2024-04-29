def l_n(caractere):
    LETRA_NUM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ0123456789'
    return caractere in LETRA_NUM #Retorna na função se o caractere digitado pelo usuário está na constante LETRA_NUM, (Sim = True) (Não = False)

def main():
    caractere = input('Escreva um caractere e veja se ele é uma letra ou número: ')

    fun_l_n = l_n(caractere)

    print(f'{fun_l_n}')

if __name__ == '__main__':
     main()
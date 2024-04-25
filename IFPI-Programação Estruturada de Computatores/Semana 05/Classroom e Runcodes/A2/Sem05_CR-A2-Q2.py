def letra(caractere):
    LETRAS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ'
    return caractere in LETRAS #Retorna na função se o caractere digitado pelo usuário está na constante LETRAS, (Sim = True) (Não = False)

def main():
    caractere = input('Escreva um caractere e veja se ele é uma letra: ')

    fun_letra = letra(caractere)

    print(f'{fun_letra}')

if __name__ == '__main__':
     main()
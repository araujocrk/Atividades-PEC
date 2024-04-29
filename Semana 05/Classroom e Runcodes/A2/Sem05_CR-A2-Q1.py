def vogal(caractere):
    VOGAIS = 'aeiouAEIOU'
    return caractere in VOGAIS #Retorna na função se o caractere digitado pelo usuário está na constante VOGAIS, (Sim = True) (Não = False)

def main():
    caractere = input('Escreva um caractere e veja se ele é uma vogal: ')

    fun_caractere = vogal(caractere)

    print(f'É uma vogal?: {fun_caractere}')

if __name__ == '__main__':
     main()
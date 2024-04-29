def vogal(carac):
    return carac.upper() in 'AEIOU'
def consoante(carac):
    return 'A' <= carac.upper() <= 'Z' not in 'AEIOU'
def numero(carac):
    return '0' <= carac <= '9'
def caractere(carac):
    return carac.upper() not in 'A' <= 'Z' and carac not in '0' <= '9' 

def main():
    carac = input('Digite um caractere: ')

    if vogal(carac):
        print('O seu caractere é uma vogal')
    elif consoante(carac):
        print('O seu caractere é uma consoante')
    elif numero(carac):
        print('O seu caractere é um número')
    elif caractere(carac):
        print('O seu caractere é um símbolo')

if __name__ == '__main__':
     main()
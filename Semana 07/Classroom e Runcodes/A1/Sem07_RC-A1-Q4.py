def vogal(carac):
    return carac.upper() in 'AEIOU'
def consoante(carac):
    return 'A' <= carac.upper() <= 'Z' not in 'AEIOU'
def numero(carac):
    return '0' <= carac <= '9'
def caractere(carac):
    return carac.upper() not in 'A' <= 'Z' and carac not in '0' <= '9' 

def main():
    carac = input()

    if vogal(carac):
        print('vogal')
    elif consoante(carac):
        print('consoante')
    elif numero(carac):
        print('número')
    elif caractere(carac):
        print('símbolo')

if __name__ == '__main__':
     main()
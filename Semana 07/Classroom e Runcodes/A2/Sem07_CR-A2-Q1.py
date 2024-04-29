def length(nome, civil, conjuge):
    if civil == '1' or civil[0].upper() == 'C':
        return len(nome) + len(conjuge)
    else:
        return len(nome)


def main():
    nome = input('Digite o seu nome: ')
    civil = input('Qual o seu estado civil? (1 - casado ou 2 - solteiro)\n')

    if civil == '1' or civil[0].upper() == 'C':
        conjuge = input('Qual o nome do seu cônjuge?\n')
        print(f'O seu nome e do seu cônjuge tem {length(nome, civil, conjuge)} caracteres')
    else:
        conjuge = 0
        print(f'O seu nome tem {length(nome, civil, conjuge)} caracteres')

if __name__ == '__main__':
    main()
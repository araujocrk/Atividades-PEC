def genero(sexo):
    if sexo == 1:
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'


def main():
    nome = input('Digite o seu nome:\n')
    sexo = int(input('Digite o seu gênero (1 - masculino ou 2 - feminino)\n'))

    print(f'Olá {genero(sexo)} {nome}')

if __name__ == '__main__':
     main()
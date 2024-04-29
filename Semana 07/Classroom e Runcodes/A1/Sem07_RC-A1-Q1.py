def genero(sexo):
    if sexo == 1:
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'


def main():
    nome = input('').strip()
    sexo = int(input().strip())

    print(f'{genero(sexo)} {nome}')

if __name__ == '__main__':
     main()
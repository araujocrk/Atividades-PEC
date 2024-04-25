def terrestre_espacial(idade_terrestre):
    idade_espacial = idade_terrestre // 2
    return idade_espacial

def main():
    idade_terrestre = int(input('Qual a sua idade em anos terrestres? '))

    print(f'Você tem {terrestre_espacial(idade_terrestre)} anos espaciais')

if __name__ == '__main__':
     main()
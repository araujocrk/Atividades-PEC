def terrestre_espacial(idade_terrestre):
    idade_espacial = idade_terrestre // 2
    return idade_espacial

def main():
    idade_terrestre = int(input().strip())

    print(f'{terrestre_espacial(idade_terrestre)}')

if __name__ == '__main__':
     main()
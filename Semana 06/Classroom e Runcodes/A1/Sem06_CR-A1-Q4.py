def maior(n1, n2, n3, n4, n5):
    max_num = max(n1, n2, n3, n4, n5)
    return max_num
def menor(n1, n2, n3, n4, n5):
    min_num = min(n1, n2, n3, n4, n5)
    return min_num
def media(n1, n2, n3, n4, n5):
    media_num = (n1 + n2 + n3 + n4 + n5) / 5
    return media_num

def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))

    print(f'Maior número: {maior(n1, n2, n3, n4, n5)}')
    print(f'Menor número: {menor(n1, n2, n3, n4, n5)}')
    print(f'Média dos números: {media(n1, n2, n3, n4, n5)}')

if __name__ == '__main__':
     main()
     
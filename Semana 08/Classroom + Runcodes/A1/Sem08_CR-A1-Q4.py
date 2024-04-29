# Cria a função mediaN que recebe 5 parâmetros e retorna a soma desses parâmetros dividido por 5
def mediaN(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():
    
    #Entrada
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))
    n4 = int(input('Digite o 4º número: '))
    n5 = int(input('Digite o 5º número: '))
    
    #Processamento
    media = mediaN(n1, n2, n3, n4, n5)
    
    #Saída
    print(f'Sua média é {media:.2f}')
# Em cada if, se as variáveis n(1-5) for maior que a variável media, imprime a mensagem na tela.
    if n1 > media:
        print(f'{n1:.2f} é maior que a média')
    if n2 > media:
        print(f'{n2:.2f} é maior que a média')
    if n3 > media:
        print(f'{n3:.2f} é maior que a média')
    if n4 > media:
        print(f'{n4:.2f} é maior que a média')
    if n5 > media:
        print(f'{n5:.2f} é maior que a média')
    
if __name__ == '__main__':
    main()
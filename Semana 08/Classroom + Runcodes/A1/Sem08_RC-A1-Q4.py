def mediaN(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():
    
    #Entrada
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    n4 = int(input().strip())
    n5 = int(input().strip())
    
    #Processamento
    media = mediaN(n1, n2, n3, n4, n5)
    
    #Saída
    print(f'{media:.2f}')
    if n1 > media:
        print(f'{n1:.2f}')
    if n2 > media:
        print(f'{n2:.2f}')
    if n3 > media:
        print(f'{n3:.2f}')
    if n4 > media:
        print(f'{n4:.2f}')
    if n5 > media:
        print(f'{n5:.2f}')
    
if __name__ == '__main__':
    main()
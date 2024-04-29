def maiorN(n1, n2, n3, n4, n5):
    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
        maior = n1
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
        maior = n2
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
        maior = n3
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
        maior = n4
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
        maior = n5
    return maior

def menorN(n1, n2, n3, n4, n5):
    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
        menor = n1
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
        menor = n2
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
        menor = n3
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
        menor = n4
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
        menor = n5
    return menor

def main():
    
    #Entrada
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    n4 = int(input().strip())
    n5 = int(input().strip())
    
    #Processamento
    maior = maiorN(n1, n2, n3, n4, n5)
    menor = menorN(n1, n2, n3, n4, n5)
    
    #Saída
    print(f'{maior}\n{menor}')
        
if __name__ == '__main__':
    main()
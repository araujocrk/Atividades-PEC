def maiorN(n1, n2, n3, n4, n5):
#Se a variável n1 for maior ou igual que n2 e n3 e n4 e n5, a variável maior recebe a variável n1 
    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
        maior = n1
#Se o comentário acima for falso, se a variável n2 for maior ou igual que n1 e n3 e n4 e n5, a variável maior recebe a variável n2 
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
        maior = n2
#Se os comentários acima for falso, se a variável n3 for maior ou igual que n1 e n2 e n4 e n5, a variável maior recebe a variável n3 
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
        maior = n3
#Se os comentários acima for falso, se a variável n4 for maior ou igual que n1 e n2 e n3 e n5, a variável maior recebe a variável n4 
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
        maior = n4
#Se os comentários acima for falso, se a variável n5 for maior ou igual que n1 e n2 e n3 e n4, a variável maior recebe a variável n5 
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
        maior = n5
#Retorno da função é a variável maior
    return maior

def menorN(n1, n2, n3, n4, n5):
#Se a variável n1 for menor ou igual que n2 e n3 e n4 e n5, a variável menor recebe a variável n1 
    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
        menor = n1
#Se o comentário acima for falso, se a variável n2 for menor ou igual que n1 e n3 e n4 e n5, a variável menor recebe a variável n2 
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
        menor = n2
#Se os comentários acima for falso, se a variável n3 for menor ou igual que n1 e n2 e n4 e n5, a variável menor recebe a variável n3 
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
        menor = n3
#Se os comentários acima for falso, se a variável n4 for menor ou igual que n1 e n2 e n3 e n5, a variável menor recebe a variável n4
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
        menor = n4
#Se os comentários acima for falso, se a variável n5 for menor ou igual que n1 e n2 e n3 e n4, a variável menor recebe a variável n5
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
        menor = n5
#Retorno da função é a variável menor
    return menor

def main():
    
    #Entrada
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))
    n4 = int(input('Digite o 4º número: '))
    n5 = int(input('Digite o 5º número: '))
    
    #Processamento
    maior = maiorN(n1, n2, n3, n4, n5)
    menor = menorN(n1, n2, n3, n4, n5)
    
    #Saída
    print(f'Dentre esses números, o maior é {maior} e o menor é {menor}')
    
if __name__ == '__main__':
    main()
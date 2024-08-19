# Função para determinar quando o loop irá parar
def flag(n):
    return n == 0
    
def main():
    maior = 0
    menor = 0
    # Estrutura de repetição que recebe um número inteiro e para que o primeiro número seja adicionado as variáveis é igualado a 0 e 
    # se o número for maior/menor que o anterior, é recebido pela variável  
    while True:
        num = int(input('Digite um número inteiro positivo:'))
        if flag(num): break 
        
        if maior == 0 or num > maior:
            maior = num
        if menor == 0 or num < menor:
            menor = num
         
    # Saída de dados
    print(f'O maior número é {maior} e o menor é {menor}')
    
if __name__ == '__main__':
    main()
# Função para determinar quando o loop irá parar
def flag(n):
    return n == 0
    
def main():
    
    soma = 0
    contador = 0
    # Estrutura de repetição que recebe uma entrada de dados e caso a entrada seja diferente de 0, a variável soma receberá a soma 
    # desse número e contador receberá mais um para calcular a média posteriormente
    while True:
        num = int(input('Digite um número inteiro positivo:'))
        if num != 0:
            soma += num
            contador += 1
        if flag(num): break  
        
    # Processamento
    media = soma / contador
    
    # Saída de dados
    print(f'A média dos seus números é {media:.2f}')
if __name__ == '__main__':
    main()
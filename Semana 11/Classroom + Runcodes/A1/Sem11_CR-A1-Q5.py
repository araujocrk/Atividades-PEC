def main():
    # Entrada de dados
    salario = float(input('Digite o valor do seu salário: R$'))
    divida = float(input('Digite o valor da sua dívida: R$'))
    # As variáveis mes e ano começam com o valor 10 e 2016
    mes = 10
    ano = 2016
    
    # Estrutura de repetição que enquanto divida for menor ou igual que o salario...
    while divida <= salario:
        # A variável mes receberá mais 1
        mes += 1
        
        # Se a variável mes passar do numero 12, voltará para o valor 1 e adicionará mais 1 ao ano
        if mes > 12:
            mes = 1
            ano += 1
        
        # Se a variável mes for igual a 3, salario aumentará 
        if mes == 3:
            salario = salario + (5 / 100 * salario)
        
        # A variável divida aumenta toda vez que é iniciada a estrutura de repetição    
        divida = divida + (15 / 100 * divida)    
    
    # Saída de dados
    print(f'Sua dívida será maior que seu salário em {mes}/{ano}')

if __name__ == '__main__':
    main()
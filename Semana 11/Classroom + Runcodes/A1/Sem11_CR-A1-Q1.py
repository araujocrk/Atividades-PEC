#Função para calcular rendimento ao ano e parar quando atingir o dobro do valor inicial
def rendimento_ao_ano(inicial,taxa):
    ano = 0
    # Variável que será o valor final 
    final = inicial * 2
    # Estrutura de repetição que tem como flag enquanto valor inicial for menor que o final, continua rodando o loop.
    while inicial < final:
        inicial = inicial + (taxa / 100 * inicial)
        ano += 1
    return ano
        
def main():
    # Entrada de dados
    inicial = float(input().strip())
    taxa = float(input().strip())
    
    # Processamento
    resultado = rendimento_ao_ano(inicial, taxa)
    
    # Saída de dados
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()
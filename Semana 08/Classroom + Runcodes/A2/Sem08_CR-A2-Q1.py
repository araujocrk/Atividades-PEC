# Define a função par5_impar8 recebendo um parâmetro
def par5_impar8(n1):
# Se o resto da divisão da variável n1 por 2 for igual a 0, retorna n1 + 5, senão retorna n1 + 8 
    if n1 % 2 == 0:
        return n1 + 5
    else:
        return n1 + 8
# Define a função par5_impar8 recebendo um parâmetro
def par_impar(n1):
# Se o resto da divisão da variável n1 por 2 for igual a 0, retorna a formatação de string 'par', senão retorna 'ímpar'
    if n1 % 2 == 0:
        return f'par'
    else:
        return f'ímpar'

def main():
    
    #Entrada
    n1 = int(input('Digite um número inteiro: '))
    
    #Processamento
    resultado = par5_impar8(n1)
    parOUimpar = par_impar(n1)
    
    #Saída
    print(f'O seu número é {parOUimpar}, então o resultado é {resultado}')
    
    
    
if __name__ == '__main__':
    main()
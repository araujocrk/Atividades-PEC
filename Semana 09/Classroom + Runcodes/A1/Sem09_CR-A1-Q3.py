# Define a função perimetro recebendo 2 parâmetros
def perimetro(b, h):
    # Retorna o valor da soma das variáveis 'b' e 'h' vezes 2
    return 2 * (b + h)
# Define a função perímetro recebendo 2 parâmetros
def area(b, h):
    # Retorna o valor da multiplicação de 'b' vezes 'h' 
    return b * h

def main():
    
    #Entrada
    b = int(input('Digite o comprimento do retângulo: '))
    h = int(input('Digite a altura do retângulo: '))
    
    #Processamento e Saída
    # Se 'b' for igual a 'h' 
    if b == h:
        # Imprime na tela a str 'Isso é um QUADRADO!'
        print(f'Isso é um QUADRADO!')
    # Se if for falso
    else:
        # Imprime a str e chama a função perimetro e area mandando 'b' e 'h' como parâmetros
        print(f'Seu perímetro é {perimetro(b, h)} e a área é {area(b, h)}')

if __name__ == '__main__':
    main()
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
    b = int(input().strip())
    h = int(input().strip())
    
    #Processamento e Saída
    # 
    if b == h:
        print(f'QUADRADO')
    else:
        print(f'{perimetro(b, h)} - {area(b, h)}')
    
if __name__ == '__main__':
    main()
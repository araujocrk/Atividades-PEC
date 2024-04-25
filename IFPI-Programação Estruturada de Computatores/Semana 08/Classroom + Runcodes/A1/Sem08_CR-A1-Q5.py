# Define a função imc recebendo dois parâmetros e retorna o calculo peso dividido pela altura elevado a 2
def imc(peso, altura):
    return peso / (altura ** 2)

def main():
    
    #Entrada
    peso = float(input('Digite o seu peso em quilos: '))
    altura = float(input('Digite sua altura em metros: '))
    
    #Processamento
    imcN = imc(peso, altura)
    
    #Saída
    print(f'{imcN:.2f}')
# Se a variável imcN for menor que 18.5, imprime a mensagem no print
    if imcN < 18.5:
        print(f'Abaixo do peso')
# Se o comentário acima for falso e imcN for maior ou igual que 18.5 e menor que 25, imprime a mensagem no print
    elif imcN >= 18.5 and imcN < 25:
        print(f'Peso normal')
# Se o comentário acima for falso e imcN for maior ou igual que 25 e menor que 30, imprime a mensagem no print
    elif imcN >= 25 and imcN < 30:
        print(f'Sobrepeso')
# Se o comentário acima for falso e imcN for maior ou igual que 30 e menor que 35, imprime a mensagem no print
    elif imcN >= 30 and imcN < 35:
        print(f'Obeso leve')
# Se o comentário acima for falso e imcN for maior ou igual que 35 e menor que 40, imprime a mensagem no print
    elif imcN >= 35 and imcN < 40:
        print(f'Obeso moderado')
# Se o comentário acima for falso e imcN for maior ou igual que 40, imprime a mensagem no print
    elif imcN >= 40:
        print(f'Obeso mórbido') 
    
if __name__ == '__main__':
    main()
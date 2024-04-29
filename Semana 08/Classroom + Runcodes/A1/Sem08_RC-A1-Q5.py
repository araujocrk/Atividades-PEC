def imc(peso, altura):
    return peso / (altura ** 2)

def main():
    
    #Entrada
    peso = float(input().strip())
    altura = float(input().strip())
    
    #Processamento
    imcN = imc(peso, altura)
    
    #Saída
    print(f'{imcN:.2f}')
    if imcN < 18.5:
        print(f'Abaixo do peso')
    elif imcN >= 18.5 and imcN < 25:
        print(f'Peso normal')
    elif imcN >= 25 and imcN < 30:
        print(f'Sobrepeso')
    elif imcN >= 30 and imcN < 35:
        print(f'Obeso leve')
    elif imcN >= 35 and imcN < 40:
        print(f'Obeso moderado')
    elif imcN >= 40:
        print(f'Obeso mórbido') 
    
if __name__ == '__main__':
    main()
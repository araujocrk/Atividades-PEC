def maior(qtd):
    maior = 0
    for i in range(qtd):
        num = int(input('Digite um número inteiro positivo: '))
        if num > maior:
            maior = num
            
    return maior

def main():
    qtd = 10
    
    resultado = maior(qtd)
    
    print(f'O maior número é o {resultado}')

if __name__ == '__main__':
    main()
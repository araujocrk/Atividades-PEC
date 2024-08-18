def main():
    soma = 0
    while True:
        n = int(input('Digite um número inteiro: '))
        if n == 0: break   
        soma += n
        
    print(f'A soma dos seus números digitos é {soma}')
    
if __name__ == '__main__':
    main()
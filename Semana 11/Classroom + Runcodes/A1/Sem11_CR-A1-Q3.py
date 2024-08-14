def flag(n):
    return n == 0
    
def main():
    maior = 0
    menor = 0
    while True:
        num = int(input('Digite um número inteiro positivo:'))
        if flag(num): break 
        
        if maior == 0 or num > maior:
            maior = num
        if menor == 0 or num < menor:
            menor = num
         
        
    print(f'O maior número é {maior} e o menor é {menor}')
if __name__ == '__main__':
    main()
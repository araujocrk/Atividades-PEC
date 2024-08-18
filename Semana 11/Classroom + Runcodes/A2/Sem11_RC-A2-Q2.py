def main():
    pessoas = 0
    soma = 0
    maior = 0
    menor = 0
    while True:
        idade = int(input().strip())
        if idade == 0: break
        pessoas += 1
        soma += idade
        media = soma / pessoas
        if maior == 0 or idade > maior:
            maior = idade
        if menor == 0 or idade < menor:
            menor = idade
        
    print(f'{pessoas}')
    print(f'{media:.2f}')
    print(f'{menor}')
    print(f'{maior}')
    
            
    
        
        
    
    
if __name__ == '__main__':
    main()
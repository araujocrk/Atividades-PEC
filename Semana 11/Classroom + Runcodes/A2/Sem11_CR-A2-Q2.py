def main():
    pessoas = 0
    soma = 0
    maior = 0
    menor = 0
    while True:
        idade = int(input('Digite sua idade: '))
        if idade == 0: break
        pessoas += 1
        soma += idade
        media = soma / pessoas
        if maior == 0 or idade > maior:
            maior = idade
        if menor == 0 or idade < menor:
            menor = idade
        
    print(f'Você digitou a idade de {pessoas}')
    print(f'A média de idade é {media:.2f}')
    print(f'A menor idade é {menor}')
    print(f'A maior idade é {maior}')
    
            
    
        
        
    
    
if __name__ == '__main__':
    main()
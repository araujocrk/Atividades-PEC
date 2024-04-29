def maior(qtd):
    maior = 0
    for i in range(qtd):
        num = int(input().strip())
        if num > maior:
            maior = num
            
    return maior

def main():
    qtd = 100
    
    resultado = maior(qtd)
    
    print(f'{resultado}')

if __name__ == '__main__':
    main()
def flag(n):
    if n == 0:
        return True
    else:
        False
    
def main():
    soma = 0
    contador = 0
    while True:
        num = int(input('Digite um número inteiro positivo:'))
        if num != 0:
            soma += num
            contador += 1
        if flag(num): break  
        
    media = soma / contador
    
    
    print(f'A média dos seus números é {media:.2f}')
if __name__ == '__main__':
    main()
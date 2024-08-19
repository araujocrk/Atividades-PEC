def main():
    total = 0
    while True:
        print(f'CÓDIGO  PRODUTO         PREÇO (R$)')
        print(f'H       Hamburger       5,50\nC       Cheeseburger    6,80\nM       Misto Quente    4,50')
        print(f'A       Americano       7,00\nQ       Queijo Prato    4,00\nX       PARA TOTAL DA CONTA')
        codigo = input().strip().upper()[0]
        if codigo == 'X': break
        if codigo != 'X' and codigo != 'H' and codigo != 'C' and codigo != 'M' and codigo != 'A' and codigo != 'Q':
            print(f'Opção inválida.')
        elif codigo == 'H':
            total += 5.5
        elif codigo == 'C':
            total += 6.8
        elif codigo == 'M':
            total += 4.5
        elif codigo == 'A':
            total += 7
        elif codigo == "Q":
            total += 4
        
    print(f'{total:.2f}')
    
        
if __name__ == '__main__':
    main()
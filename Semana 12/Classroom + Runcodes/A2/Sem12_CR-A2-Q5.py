def eh_primo(n):
    primo = 0
    
    for c in range(1, n + 1):
        if n % c == 0:
            primo += 1
    
    return primo == 2
    
def main():
    
    x = int(input(f'Digite o valor de x: '))
    y = int(input(f'Digite o valor de y: '))
    
    if x > y:
        x, y = y, x
    
    for c in range(x, y + 1):
        if eh_primo(c):
            print(f'{c}')
    
if __name__ == "__main__":
    main()
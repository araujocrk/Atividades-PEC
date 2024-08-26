def eh_primo(n):
    primo = 0
    
    for c in range(1, n + 1):
        if n % c == 0:
            primo += 1
    
    if primo == 2:
        return 'é primo'
    else:
        return 'não é primo'
    
def main():
    
    num = int(input(f'Digite um número para saber se é primo: '))
    
    resultado = eh_primo(num)
    
    print(f'O seu número {resultado}')
if __name__ == "__main__":
    main()
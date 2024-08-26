def eh_primo(n):
    primo = 0
    
    for c in range(1, n + 1):
        if n % c == 0:
            primo += 1
    
    return primo == 2
    
def main():
    
    num = int(input().strip())
    
    resultado = eh_primo(num)
    
    print(f'{resultado}')
if __name__ == "__main__":
    main()
def main():
    soma = 0
    while True:
        n = int(input().strip())
        if n == 0: break   
        soma += n
        
    print(f'{soma}')

if __name__ == '__main__':
    main()
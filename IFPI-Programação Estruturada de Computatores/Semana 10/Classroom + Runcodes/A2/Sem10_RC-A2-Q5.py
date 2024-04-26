def parcelas(i, f, m):
    for p in range(i, f):
        print(f'{p}x de R$ {m / p:.2f}')

def main():
    preco = float(input().strip())
    parcelas(1, 25, preco)
    
if __name__ == '__main__':
    main()
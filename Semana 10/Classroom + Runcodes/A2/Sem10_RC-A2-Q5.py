def parcelas(i, f, v):
    for p in range(i, f):
        print(f'{p}x de R$ {v / p:.2f}')

def main():
    preco = float(input().strip())
    parcelas(1, 25, preco)
    
if __name__ == '__main__':
    main()

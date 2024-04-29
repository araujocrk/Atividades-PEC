def parcelas(i, f, v):
    for p in range(i, f):
        print(f'{p}x de R$ {v / p:.2f}')

def main():
    preco = float(input('Digite o preço do seu produto').strip())
    parcelas(1, 25, preco)
    
if __name__ == '__main__':
    main()

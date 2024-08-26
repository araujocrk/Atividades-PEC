def calcular_H(n):
    h = 0
    for c in range(1, n + 1):
        h = h + (1 / c)
        
    return h
def main():
    
    num = int(input(f'Digite o valor de n: '))
    
    resultado = calcular_H(num)
    
    print(f'O resultado de H é {resultado:.4f}')
       
if __name__ == "__main__":
    main()
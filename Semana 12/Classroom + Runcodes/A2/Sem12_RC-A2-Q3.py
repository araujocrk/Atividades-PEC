def calcular_H(n):
    h = 0
    for c in range(1, n + 1):
        h = h + (1 / c)
        
    return h
def main():
    
    num = int(input('').strip())
    
    resultado = calcular_H(num)
    
    print(f'{resultado:.4f}')
       
if __name__ == "__main__":
    main()
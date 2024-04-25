def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b

def main():
    
    #Entrada
    n1 = float(input().strip())
    n2 = float(input().strip())
    op = int(input().strip())
    
    #Processamento
    if op == 1:
        resultado = adicao(n1, n2)
    elif op == 2:
        resultado = subtracao(n1, n2)
    elif op == 3:
        resultado = multiplicacao(n1, n2)
    elif op == 4:
        resultado = divisao(n1, n2)
    
    #Saída
    print(f'{resultado:.2f}')
    
    
    
if __name__ == '__main__':
    main()
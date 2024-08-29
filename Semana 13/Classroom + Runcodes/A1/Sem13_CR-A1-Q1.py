def ler_num(q):
    N = []
    for c in range(q):
        N.append(int(input(f'Digite o {c + 1}º número: ')))
    return N

def somar_num(n):
    return sum(n)

def multiplicar_num(n):
    multi = 1
    for c in n:
        multi *= c
    return multi    
    
def main():
    
    numeros = ler_num(10)
    print(numeros)
    print(somar_num(numeros))
    print(multiplicar_num(numeros))
    
if __name__ == "__main__":
    main()
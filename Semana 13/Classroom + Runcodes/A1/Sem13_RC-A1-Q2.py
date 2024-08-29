def preencher_lista_0(n):
    lista_0 = []
    for c in range(n):
        lista_0.append(0)
    return lista_0
    
def preencher_1_n(n):
    lista_1 = []
    for c in range(1, n + 1):
        lista_1.append(c)
    return lista_1

def preencher_input(n):
    lista_input = []
    for c in range(n):
        lista_input.append(int(input().strip()))
    return lista_input
    
def preencher_inverso(n):
    lista_inversa = []
    for c in range(n):
        lista_inversa.insert(0, int(input().strip()))
    return lista_inversa

def main():

    numero = int(input().strip())
    print(preencher_lista_0(numero))
    print(preencher_1_n(numero))
    print(preencher_input(numero))
    print(preencher_inverso(numero))
    
if __name__ == "__main__":
    main()
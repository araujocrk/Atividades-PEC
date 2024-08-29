def ler_num_0():
    N = []
    while True:
        n = int(input().strip())
        if n == 0: break
        N.append(n)
    return N
    
def multiplica_constantes(N, CONSTANTE):
    lista_constante = []
    for c in range(len(N)):
        lista_constante.append(N[c] * CONSTANTE)
    return lista_constante
def main():
    
    N = ler_num_0()
    CONSTANTE = int(input().strip())
    
    print(multiplica_constantes(N, CONSTANTE))
    
if __name__ == "__main__":
    main()
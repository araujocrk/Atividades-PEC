def ler_num_0():
    N = []
    while True:
        n = int(input('Digite um número inteiro para adicionar na lista("0" para parar): '))
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
    CONSTANTE = int(input('Digite um valor para multiplicar cada item de sua lista: '))
    
    print(multiplica_constantes(N, CONSTANTE))
    
if __name__ == "__main__":
    main()
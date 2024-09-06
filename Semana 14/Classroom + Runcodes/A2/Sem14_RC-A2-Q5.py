def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
        lista.append(elemento)
    return lista

def listaUnidaSemRepetir(A, B):
    C = []
    for i in range(len(A)):
        if A[i] not in C:
            C.append(A[i])
    for i in range(len(B)):
        if B[i] not in C:
            C.append(B[i])
    return C

def main():

    A = carregarLista(10)
    B = carregarLista(10)
    print(f'{listaUnidaSemRepetir(A, B)}')

if __name__ == '__main__':
    main()
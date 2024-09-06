def carregarLista(q, nome):
    lista = []
    for i in range(q):
        elemento = int(input(f'Adicione o {i + 1}º elemento da lista {nome}: ').strip())
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

    A = carregarLista(10, 'A')
    B = carregarLista(10, 'B')
    print(f'Lista A:\n{A}')
    print(f'Lista B:\n{B}')
    print(f'Lista A + B sem repetir números:\n{listaUnidaSemRepetir(A, B)}')


if __name__ == '__main__':
    main()
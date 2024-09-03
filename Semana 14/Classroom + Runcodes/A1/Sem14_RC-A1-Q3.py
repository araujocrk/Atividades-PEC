def carrega_lista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
        lista.append(elemento)
    return lista

def soma_duas_listas(A, B):
    C = []
    for i in range(len(A)):
        C.append(A[i] + B[i])
    return C

def main():
    A = carrega_lista(20)
    B = carrega_lista(20)
    C = soma_duas_listas(A, B)
    print(f'{A}\n{B}\n{C}')
if __name__ == '__main__':
    main()
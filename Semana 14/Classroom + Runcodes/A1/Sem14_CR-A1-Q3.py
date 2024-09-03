def carrega_lista(q, nome):
    lista = []
    for i in range(q):
        elemento = int(input(f'Adicione o {i + 1}º elemento da lista {nome}: ').strip())
        lista.append(elemento)
    return lista

def soma_duas_listas(A, B):
    C = []
    for i in range(len(A)):
        C.append(A[i] + B[i])
    return C

def main():
    A = carrega_lista(20, 'A')
    B = carrega_lista(20, 'B')
    C = soma_duas_listas(A, B)
    print(f'A soma da lista A:\n{A}\nMais a lista B:\n{B}\nÉ igual a lista C:\n{C}')
if __name__ == '__main__':
    main()
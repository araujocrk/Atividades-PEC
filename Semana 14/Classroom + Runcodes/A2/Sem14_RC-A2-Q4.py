def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
        lista.append(elemento)
    return lista

def produtoEscalar(X, Y):
    prodEsc = 0
    multiAtual = 0
    for i in range(len(X)):
        multiAtual = X[i] * Y[i]
        prodEsc += multiAtual
    return prodEsc

def main():

    X = carregarLista(5)
    Y = carregarLista(5)
    print(f'{X}')
    print(f'{Y}')
    print(f'({X[0]} x {Y[0]}) + ({X[1]} x {Y[1]}) + ({X[2]} x {Y[2]}) + ({X[3]} x {Y[3]}) + ({X[4]} x {Y[4]}) = {produtoEscalar(X, Y)}')

if __name__ == '__main__':
    main()
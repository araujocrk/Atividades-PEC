def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input(f'Adicione o {i + 1}º elemento da lista: ').strip())
        lista.append(elemento)
    return lista

def listaSemRepetidos(l):
    semRepetidos = []
    for e in l:
        if e not in semRepetidos:
            semRepetidos.append(e)
    return semRepetidos

def main():

    listaInt = carregarLista(10)
    print(f'Sua lista:\n{listaInt}')
    print(f'Sua lista sem números repitidos:\n{listaSemRepetidos(listaInt)}')

if __name__ == '__main__':
    main()
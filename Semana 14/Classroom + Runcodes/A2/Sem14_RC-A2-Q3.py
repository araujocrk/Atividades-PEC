def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
        lista.append(elemento)
    return lista

def listaSemRepetidos(l):
    semRepetidos = []
    for e in l:
        if e not in semRepetidos:
            semRepetidos.append(e)
    return semRepetidos

def main():

    listaInt = carregarLista(20)
    print(f'{listaSemRepetidos(listaInt)}')

if __name__ == '__main__':
    main()
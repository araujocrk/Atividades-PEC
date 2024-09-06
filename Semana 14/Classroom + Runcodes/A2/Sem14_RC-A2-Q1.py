def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
        lista.append(elemento)
    return lista

def maiorElemento(l):
    return max(l)

def indiceMaiorElemento(l):
    return l.index(maiorElemento(l))

def main():
    
    listaInt = carregarLista(10)
    print(f'{listaInt}')
    print(f'{maiorElemento(listaInt)}')
    print(f'{indiceMaiorElemento(listaInt)}')
    
if __name__ == '__main__':
    main()
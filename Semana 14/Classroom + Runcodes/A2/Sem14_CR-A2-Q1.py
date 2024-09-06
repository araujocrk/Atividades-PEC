def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input(f'Adicione o {i + 1}º elemento da lista: ').strip())
        lista.append(elemento)
    return lista

def maiorElemento(l):
    return max(l)

def indiceMaiorElemento(l):
    return l.index(maiorElemento(l)) + 1

def main():
    
    listaInt = carregarLista(10)
    print(f'Sua lista:\n{listaInt}')
    print(f'Maior elemento da lista: {maiorElemento(listaInt)}')
    print(f'Posição do maior elemento: {indiceMaiorElemento(listaInt)}')
    
if __name__ == '__main__':
    main()
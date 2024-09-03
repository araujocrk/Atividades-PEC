def carrega_lista():
    lista = []
    c = 1
    while True:
        elemento = int(input().strip())
        c += 1
        if elemento == 0: break
        lista.append(elemento)
    return lista
    
def contar(l, p):
    quantidade = 0
    for c in l:
        if c == p:
            quantidade += 1
    return quantidade

def main():
    lista = carrega_lista()
    pesquisar = int(input().strip())
    print(lista)
    print(pesquisar)
    print(contar(lista, pesquisar))

if __name__ == '__main__':
    main()
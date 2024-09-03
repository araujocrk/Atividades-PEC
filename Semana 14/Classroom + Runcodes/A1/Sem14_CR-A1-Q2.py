def carrega_lista():
    lista = []
    c = 1
    while True:
        elemento = int(input(f'Adicione o {c}º elemento da lista(0 para parar): ').strip())
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
    pesquisar = int(input(f'Digite o valor que deseja pesquisar: ').strip())
    print(f'Na lista:\n{lista}\nO valor {pesquisar} aparece {contar(lista, pesquisar)} vezes')

if __name__ == '__main__':
    main()
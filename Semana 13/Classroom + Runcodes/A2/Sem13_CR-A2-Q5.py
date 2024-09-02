def preencher_lista(q):
    L = []
    for c in range(q):
        valor = input(f'Digite o {c + 1}º valor da lista: ').strip()
        try:
            numero = int(valor)
            L.append(numero)
        except ValueError:
            try:
                numero = float(valor)
                L.append(numero)
            except ValueError:
                L.append(valor)
    return L

def esta_ordenada(lista):
    for c in range(len(lista) - 1):
        if lista[c] > lista[c + 1]:
            return False
    return True

def main():
    quantidade = int(input(f'Digite a quantidade de elementos da lista: ').strip())
    L = preencher_lista(quantidade)
    esta_ordenada(L)
    if esta_ordenada(L):
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')
        
if __name__ == "__main__":
    main()

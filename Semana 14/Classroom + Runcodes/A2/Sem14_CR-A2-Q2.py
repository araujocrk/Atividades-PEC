def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = float(input(f'Adicione o {i + 1}º elemento da lista: ').strip())
        lista.append(elemento)
    return lista

def qntNegativos(l):
    contador = 0
    for e in l:
        if e < 0:
            contador += 1
    return contador 

def numPositivos(l):
    positivos = []
    for e in l:
        if e > 0:
            positivos.append(e)
    return positivos

def somaPositivos(l):
    pos = numPositivos(l)
    soma = 0
    for e in pos:
        soma += e
    return soma

def main():
    
    listaFloat = carregarLista(10)
    print(f'Sua lista:\n{listaFloat}')
    print(f'Quantidade de números negativos: {qntNegativos(listaFloat)}')
    print(f'A soma dos números positivos: {somaPositivos(listaFloat)}')
    
    
if __name__ == '__main__':
    main()
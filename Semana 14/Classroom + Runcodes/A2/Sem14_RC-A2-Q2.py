def carregarLista(q):
    lista = []
    for i in range(q):
        elemento = int(input().strip())
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
    print(f'{listaFloat}')
    print(f'{qntNegativos(listaFloat)}')
    print(f'{somaPositivos(listaFloat)}')
    
    
if __name__ == '__main__':
    main()
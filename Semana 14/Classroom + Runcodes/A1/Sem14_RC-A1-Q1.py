def carrega_lista():
    lista = []
    while True:
        elemento = int(input().strip())
        if elemento == 0: break
        lista.append(elemento)
    return lista
    
def comprimento(l):
    length = 0
    for i in l:
        length += 1
    return length

def inverter(l):
    invertida = []
    for e in l:
        invertida.insert(0, e)
    return invertida

def minimo(l):
    minimo = l[0]
    for e in l:
        if e < minimo:
            minimo = e
    return minimo

def maximo(l):
    maximo = l[0]
    for e in l:
        if e > maximo:
            maximo = e
    return maximo

def soma(l):
    soma = 0
    for e in l:
        soma += e
    return soma

def main():
    lista = carrega_lista()
    print(lista)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == '__main__':
    main()
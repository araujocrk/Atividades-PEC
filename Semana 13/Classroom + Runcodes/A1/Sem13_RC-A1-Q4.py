def preencher_num(n):
    N = []
    for c in range(n):
        N.append(int(input().strip()))
    return N

def lista_par(lista):
    P = []
    for c in lista:
        if c % 2 == 0:
            P.append(c)
    return P

def lista_impar(lista):
    I = []
    for c in lista:
        if c % 2 != 0:
            I.append(c)
    return I

def main():
    lista_num = preencher_num(20)
    print(f'{lista_num}')
    print(f'{lista_par(lista_num)}')
    print(f'{lista_impar(lista_num)}')

if __name__ == '__main__':
    main()
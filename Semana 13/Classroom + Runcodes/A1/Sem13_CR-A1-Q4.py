def preencher_num(n):
    N = []
    for c in range(n):
        N.append(int(input(f'Digite o {c + 1}º número para armazenar na lista: ')))
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
    print(f'Lista com os 20 números:\n{lista_num}')
    print(f'Lista com os números pares{lista_par(lista_num)}')
    print(f'Lista com os números ímpares{lista_impar(lista_num)}')
    
        
        
if __name__ == '__main__':
    main()
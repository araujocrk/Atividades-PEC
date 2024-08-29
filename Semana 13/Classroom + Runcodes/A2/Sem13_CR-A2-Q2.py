def ler_num(q):
    N = []
    for c in range(q):
        N.append(int(input(f'Digite o {c + 1}º número da lista: ').strip()))
    return N

def ordernar_lista(N):
    N_ord = N[:]
    N_ord.sort()
    return N_ord

def multiplicar_num(N_ord):
    M = []
    for i in range(len(N_ord)):
        if i % 2 == 0:
            M.append(N_ord[i] * 3)
        else:
            M.append(N_ord[i] * 5)
    return M
        
def main():
    N = ler_num(100)
    N_ordenada = ordernar_lista(N)
    print(f'Sua lista ordenada por índices multiplicada por 3 (caso seja par) e 5 (caso seja impar):\n{multiplicar_num(N_ordenada)}')
    
if __name__ == "__main__":
    main()
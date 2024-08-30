def preencher_lista():
    N = []
    while True:
        num = int(input().strip())
        if num == 0: break
        N.append(num)
    return N

def soma_acumulativa(N):
    S = []
    for c in range(len(N)):
        if c == 0: 
            S.append(N[c])
        else:
            S.append(N[c] + S[c - 1])
    return S

def main():
    
    lista = preencher_lista()
    print(soma_acumulativa(lista))
    
if __name__ == "__main__":
    main()
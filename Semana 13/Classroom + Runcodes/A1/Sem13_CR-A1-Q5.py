def lista_A(n):
    A = []
    for c in range(n):
        A.append(int(input(f'Digite o {c + 1}º valor da lista A: ')))
    return A

def lista_B(n):
    B = []
    for c in range(n):
        B.append(int(input(f'Digite o {c + 1}º valor da lista B: ')))
    return B

def lista_C(A, B):
    C = []
    for c in range(len(A)):
        C.append(A[c])
        C.append(B[c])
    return C 
        
def main():
    
    A = lista_A(25)
    B = lista_B(25)
    C = lista_C(A, B)
    print(f'Lista A:\n{A}')
    print(f'Lista B:\n{B}')
    print(f'Lista C:\n{C}')
    
    
        
        
if __name__ == '__main__':
    main()
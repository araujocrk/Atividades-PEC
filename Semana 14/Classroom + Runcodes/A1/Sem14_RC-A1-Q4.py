def nome_altura(q):
    nome = []
    altura = []
    for i in range(q):
        n = input().strip()
        nome.append(n)
        a = float(input().strip())
        altura.append(a)
    return nome, altura

def maior(N, A):
    maior = A.index(max(A))
    return N[maior], A[maior]

def media(A):
    return sum(A) / len(A)

def maior_media(N, A, media):
    nome_m_m = []
    altura_m_m = []
    for i in range(len(N)):
        if A[i] > media:
            nome_m_m.append(N[i])
            altura_m_m.append(A[i])
    return nome_m_m, altura_m_m


def main():
    N, A = nome_altura(12)
    
    nome_maior, maior_altura = maior(N, A)
    print(f'JOGADOR MAIS ALTO DO TIME\n{nome_maior}\n{maior_altura:.2f}')
    
    alturaMedia = media(A)
    print(f'ALTURA MÉDIA DO TIME\n{alturaMedia:.2f}')
    
    nome_m_m, altura_m_m = maior_media(N, A, alturaMedia)
    print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    
    for e in range(len(nome_m_m)):
        print(f'{nome_m_m[e]}\n{altura_m_m[e]:.2f}')

if __name__ == '__main__':
    main()
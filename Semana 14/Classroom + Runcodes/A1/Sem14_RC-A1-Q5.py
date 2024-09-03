def nome_idade_altura(q):
    nome = []
    idade = []
    altura = []
    for i in range(q):
        n = input().strip()
        nome.append(n)
        
        yo = int(input().strip())
        idade.append(yo)
        
        a = float(input().strip())
        altura.append(a)
        
    return nome, idade, altura

def media(A):
    return round(sum(A) / len(A), 2)

def menor_media_w_13(N, I, A, media):
    alunos = []
    for i in range(len(I)):
        if I[i] > 13:
            if A[i] < media:
                alunos.append(N[i])
    return alunos

def main():
    N, I, A = nome_idade_altura(30)
    mediaAltura = media(A)
    alunos = menor_media_w_13(N, I, A, mediaAltura)
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for e in range(len(alunos)):
        print(alunos[e])

if __name__ == '__main__':
    main()
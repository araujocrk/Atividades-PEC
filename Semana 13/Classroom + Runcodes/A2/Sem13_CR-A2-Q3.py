def ler_notas(q):
    N = []
    for c in range(q):
        N.append(float(input(f'Digite a {c + 1}º nota: ')))
    return N
        
def maior_igual_6(n):
    M = []
    I = []
    for i in range(len(n)):
        if n[i] >= 6:
            M.append(n[i])
            I.append(i)
    return M, I

def main():
    notas = ler_notas(50)
    M, I = maior_igual_6(notas)
    print(f'Notas maiores ou iguais que 6:\n{M}')
    print(f'Índices das notas maiores ou iguais que 6:\n{I}')
if __name__ == "__main__":
    main()
def ler_notas(q):
    N = []
    for c in range(q):
        N.append(float(input().strip()))
    return N
        
def maior_igual_6(n):
    I = []
    for i in range(len(n)):
        if n[i] >= 6:
            I.append(i)
    return I

def main():
    notas = ler_notas(50)
    print(maior_igual_6(notas))

if __name__ == "__main__":
    main()
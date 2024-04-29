def crescente(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        maior = n1
        if n2 > n3:
            medio = n2
            menor = n3
        else:
            medio = n3
            menor = n2
        return f'{menor}\n{medio}\n{maior}'
    elif n2 > n1 and n2 > n3:
        maior = n2
        if n1 > n3:
            medio = n1
            menor = n3
        else:
            medio = n3
            menor = n1
        return f'{menor}\n{medio}\n{maior}'
    elif n3 > n1 and n3 > n2:
        maior = n3 
        if n1 > n2:
            medio = n1
            menor = n2
        else:
            medio = n2
            menor = n1
        return f'{menor}\n{medio}\n{maior}'

def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())

    print(f'{crescente(n1, n2, n3)}')

if __name__ == '__main__':
     main()
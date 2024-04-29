def mf(n1, n2, n3, me):
    return (n1 + (n2 * 2) + (n3 * 3) + me) / 7

def conceito(n1, n2, n3, me):
    medfin = mf(n1, n2, n3, me)
    A = medfin >= 9
    B = 7.5 <= medfin < 9
    C = 6 <= medfin < 7.5
    D = 4 <= medfin < 6
    E = medfin < 4
    if A and B and C:
        return f'A, B e C\nAprovado'
    elif A and B:
        return f'A e B\nAprovado'
    elif A and C:
        return f'A e C\nAprovado'
    elif B and C:
        return f'B e C\nAprovado'
    elif A:
        return f'A\nAprovado'
    elif B:
        return f'B\nAprovado'
    elif C:
        return f'C\nAprovado'
    elif D and E:
        return f'D e E\nReprovado'
    elif D:
        return f'D\nReprovado'
    elif E:
        return f'E\nReprovado'
        
def main():
    
    #Entrada
    matricula = input().strip()
    n1 = float(input().strip())
    n2 = float(input().strip())
    n3 = float(input().strip())
    me = float(input().strip())
    
    #Processamento
    media_final = mf(n1, n2, n3, me)
    resultado = conceito(n1, n2, n3, me)

    #Saída
    print(f'{matricula}\n{media_final:.2f}\n{resultado}')
         
if __name__ == '__main__':
    main()
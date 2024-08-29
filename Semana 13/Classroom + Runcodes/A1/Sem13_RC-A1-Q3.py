def preencher_reais(n):
    lista_reais = []
    for c in range(n):
        add = round(float(input().strip()), 4)
        lista_reais.insert(0, add)
    return lista_reais

def preencher_notas(n):
    lista_notas = []
    for c in range(n):
        nota = round(float(input().strip()), 1)
        lista_notas.append(nota)
    return lista_notas

def media(lista):
    return sum(lista) / len(lista)

def preencher_letras(n):
    lista_consoantes = []
    vogal = 0
    for c in range(n):
        letra = input().strip()
        if letra in 'aeiouAEIOU':
            vogal += 1
        else:
            lista_consoantes.append(letra)
    return vogal, lista_consoantes

def main():
    notas = []
    num = int(input().strip())
    print(f'{preencher_reais(num)}')
    notas = preencher_notas(num)
    print(f'{notas}')
    if num != 0:
        print(f'{media(notas):.1f}')
    else:
        print('SEM NOTAS')
    vogal, consoantes = preencher_letras(num)
    print(f'{vogal}')
    print(f'{consoantes}')
        
if __name__ == '__main__':
    main()
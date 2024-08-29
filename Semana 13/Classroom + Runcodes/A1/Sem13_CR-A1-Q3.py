def preencher_reais(n):
    lista_reais = []
    for c in range(n):
        add = round(float(input(f'Digite o {c + 1}º número real da lista inversa: ').strip()), 4)
        lista_reais.insert(0, add)
    return lista_reais

def preencher_notas(n):
    lista_notas = []
    for c in range(n):
        nota = round(float(input(f'Digite a {c + 1}ª nota: ')), 1)
        lista_notas.append(nota)
    return lista_notas

def media(lista):
    return sum(lista) / len(lista)

def preencher_letras(n):
    lista_consoantes = []
    vogal = 0
    for c in range(n):
        letra = input(f'Digite a {c + 1}ª letra: ')
        if letra in 'aeiouAEIOU':
            vogal += 1
        else:
            lista_consoantes.append(letra)
    return vogal, lista_consoantes

def main():
    notas = []
    num = int(input('Digite um número inteiro: '))
    print(f'Lista de números reais:\n{preencher_reais(num)}')
    notas = preencher_notas(num)
    print(f'Lista de notas:\n{notas}')
    if num != 0:
        print(f'Média das notas: {media(notas):.1f}')
    else:
        print('SEM NOTAS')
    vogal, consoantes = preencher_letras(num)
    print(f'Você digitou {vogal} vogais.')
    print(f'Lista de consonates:\n{consoantes}')
        
if __name__ == '__main__':
    main()
from random import *

executa = True
nome_femea = ['Lua', 'Luna', 'Mia', 'Nina', 'Pandora', 'Nala', 'Mel', 'Belinha']
nome_macho = ['Chico', 'Fred', 'Simba', 'Theo', 'Thor', 'Zeus', 'Max', 'Hulk']

print('Serviço de escolha de nome para animais de estimação')
print('-----------------------')
print('''
Menu
    n = obter nome do animal
    am = adicionar nome do animal macho 
    af = adicionar nome do animal fêmea
    dm = remover nome do animal macho
    df = remover nome do animal femea
    pm = imprimir nomes dos animais machos
    pf = imprimir nomes dos animais fêmeas 
    q = sair
''')


masc = 0
fem = 0

while executa == True:
    menuChoice = input('\n>_').lower()
    if menuChoice == 'n':
        qtd = int(input('Quantos animais você tem?: '))
        for i in range(qtd):
            genero = input(f'Qual é o gênero do seu {i + 1}º animal? (masculino ou feminino): ').lower()
            if genero[0] == 'm':
                masc += 1
            elif genero[0] == 'f':
                fem += 1
            else:
                print('Opção inválida! Tente novamente.') 
                break
        for i in range(masc):
            print(choice(nome_macho))
        for i in range(fem):
            print(choice(nome_femea))
        masc = 0
        fem = 0
    elif menuChoice == 'am':
        machoToAdd = input('Adicione um nome de animal macho: ')
        if machoToAdd not in nome_macho:
            nome_macho.append(machoToAdd)
        else:
            print('O nome de animal macho já está na lista!')
    elif menuChoice == 'af':
        femeaToAdd = input('Adicione um nome de animal fêmea: ')
        if femeaToAdd not in nome_femea:
            nome_femea.append(femeaToAdd)
        else:
            print('O nome de animal femea já está na lista!')
    elif menuChoice == 'dm':
        machoToDelete = input('Insira o nome de um animal macho a ser removido: ')
        if machoToDelete in nome_macho:
            nome_macho.remove(machoToDelete)
        else:
            print('O nome de animal macho não está na lista!')
    elif menuChoice == 'df':
        femeaToDelete = input('Insira o nome de um animal fêmea a ser removido: ')
        if femeaToDelete in nome_femea:
            nome_femea.remove(femeaToDelete)
        else:
            print('O nome de animal fêmea não está na lista!')
    elif menuChoice == 'pm':
        print('Nomes dos animais machos:')
        print(nome_macho)
    elif menuChoice == 'pf':
        print('Nomes dos animais femeas:')
        print(nome_femea)
    elif menuChoice == 'q':
        executa = False
    else:
        print('Opção inválida! Tente novamente.')
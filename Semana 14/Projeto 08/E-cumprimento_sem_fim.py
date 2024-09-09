from random import *

executa = True

adjetivos = ['maravilhoso', 'acima da média', 'excelente']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

print('Gerador de cumprimentos')
print('-----------------------')

nome = input('Qual é o seu nome?: ')

print('''
Menu 
    c = obter cumprimento
    q = sair
''')

while executa == True:
    menuChoice = input('\n>_').lower()
    
    if menuChoice == 'c':
        
        print('Aqui está o seu cumprimento', nome, ':')
        print(f'{nome} você é {choice(adjetivos)} em {choice(hobbies)}')
        print('De nada!')
        
    elif menuChoice == 'q':
        executa = False
    else:
        print('Escolha uma opção válida!')
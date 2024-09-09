from random import *

print('Gerador de cumprimentos')
print('-----------------------')

adjetivos = ['maravilhoso', 'acima da média', 'excelente', 'brilhante', 'fantástico']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'jogar', 'pintar']

nome = input('Digite é o seu nome: ')

print('Aqui está o seu cumprimento', nome, ':')
print(f'{nome} você é {choice(adjetivos)} em {choice(hobbies)}')
print('De nada!')
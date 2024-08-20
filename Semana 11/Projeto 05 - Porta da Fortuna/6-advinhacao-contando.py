from random import *

score = 0
print('''
    Porta da Fortuna!
    ===========
      
    Existe um super prêmio atrás de uma destas 3 portas!
    Advinhe qual é a porta certa para ganhar o prêmio
    
        _____     _____     _____
       |     |   |     |   |     |
       | [1] |   | [2] |   | [3] |
       |   o |   |   o |   |   o |
       |_____|   |_____|   |_____|
      ''')

for attempt in range(3):
    
    print('\nEscolha uma porta (1, 2 ou 3):')

    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
        
    portaCerta = randint(1,3)

    print('A porta escolhida foi', portaEscolhida)
    print('A porta certa é a', portaCerta)
    
    
    if portaEscolhida == portaCerta:
        print(f'Parabéns!')
        score += 1
    else:
        print(f'Que peninha!')
        
print(f'Você acertou a porta {score} vezes')
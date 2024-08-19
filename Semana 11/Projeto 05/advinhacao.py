from random import *

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

    Escolha uma porta (1, 2 ou 3):
      ''')

portaEscolhida = input()
portaEscolhida = int(portaEscolhida)
    
portaCerta = randint(1,3)

print('A porta escolhida foi', portaEscolhida)
print('A porta certa é a', portaCerta)

if portaEscolhida == portaCerta:
    print(f'Parabéns!')
else:
    print(f'Que peninha!')
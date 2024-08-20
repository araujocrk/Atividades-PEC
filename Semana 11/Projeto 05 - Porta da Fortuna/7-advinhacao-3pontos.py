from random import *

tentativas = 0
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


while score < 3:
    
    tentativas += 1
    
    print(f'\nTentativa {tentativas}: Escolha uma porta (1, 2 ou 3):')

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
        
        
    print(f'Sua pontuação atual é {score}.')
    
print(f'Você conseguiu! Terminou o jogo em {tentativas} tentativas')
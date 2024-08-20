from random import *

jogando = True
prox_num = 0
num_atual = 0

print('''
    Vinte e um!
    ===========
    Tente fazer exatamente 21 pontos!  
      ''')

while jogando == True:
    
    prox_num = randint(1, 10)
    num_atual += prox_num
    print(f'Seu próximo número é {prox_num}')
    print(f'Sua pontuação atual é {num_atual}\n')
    
    resposta = input('Gostaria de somar mais um número? (s/n)\n').lower()[0]
    if resposta == 'n':
        jogando = False
        
print(f'\nSua pontuação final é {num_atual}')
if num_atual == 21:
    print(f'VCCÊ VENCEU!!')
else:
    print(f'Que pena!!')

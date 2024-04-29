print('Qual o meu jogo favorito?')
resposta = input()

if resposta.lower() == 'counter strike global offensive' or resposta.lower() == 'csgo':
    print('Acertou! Você me conhece mesmo :)')
elif resposta.lower() == 'cs' or resposta.lower() == 'cs2' or resposta.lower() == 'counter-strike' or resposta.lower() == 'counter strike 2':
    print('Foi quase!')
else:
    print('Não foi dessa vez :(')

print('Obrigado por jogar!')
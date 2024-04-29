def main():
    
    print('''
1) Qual o meu jogo favorito?

a) Project Zomboid
b) The Last of Us
c) Counter Strike: Global Offensive''')
    score = 0
    resposta1 = input('R: ').lower()

    if resposta1 == 'a':
        print('Estou jogando muito mas não.')
    elif resposta1 == 'b':
        print('Belíssima resposta mas não.')
    elif resposta1 == 'c':
        score += 1
        print('É claro, meu jogo mais jogado!')
    else:
        print('Você não escolheu entre as alternativas!')

    print('''
2) Qual a série que estou assistindo no momento? (01/04/24)

a) House of the Dragon
b) The Walking Dead
c) Avatar: The Last Airbender''')
    resposta2 = input('R: ').lower()
    
    if resposta2 == 'a':
        print('Não! Ainda pretendo assistir!!!')
    elif resposta2 == 'b':
        score += 1
        print('Exatoo! Estou reassistindo em inglês.')
    elif resposta2 == 'c':
        print('Já assisti! Muito bom por sinal.')
    else:
        print('Você não escolheu entre as alternativas!')
        
    print('''
3) Qual jogo estou mais assistindo no momento? (03/24)

a) Counter Strike 2
b) Project Zomboid
c) League of Legends''')
    resposta3 = input('R: ').lower()
    
    if resposta3 == 'a':
        print('Assisti muito mas não.')
    elif resposta3 == 'b':
        print('Já assisti muito ano passado!')
    elif resposta3 == 'c':
        score += 1
        print('CBLOL no IDL é bom demais, TOMA GAP!')
    else:
        print('Você não escolheu entre as alternativas!')
    
    print(f'Seu resultado foi {score}/3')
    if score == 0:
        print('Tente novamente!')
    elif 0 < score < 3:
        print('Você foi mais ou menos.')
    else:
        print('Muito bem, você me conhece mesmo!')
    saida = input('Clique em ENTER para sair.')
if __name__ == '__main__':
    main()
print('''
      Qual o meu jogo favorito?
      a) Counter Strike 2
      b) The Last of Us
      c) Counter Strike: Global Offensive
      d) Fortnite 
      e) Project Zomboid
      ''')
resposta = input().lower()

if resposta == 'c':
    print('Acertou! Você me conhece mesmo! :)')
elif resposta == 'a':
    print('Meu pc não rodou mais, ou seja, NÃO! ;(')
elif resposta == 'b':
    print('Belíssima resposta mas não. :(')
elif resposta == 'd':
    print('Nunca fui bem com construção haha, não!')
elif resposta == 'e':
    print('Tenho jogado muito mas não. :(')
else:
    print('Você não escolheu entre as alternativas!')

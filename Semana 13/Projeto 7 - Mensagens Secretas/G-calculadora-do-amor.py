def main():
    
    print('''
Calculadora do amor
<3 <3 <3 <3 <3 <3 <3
          ''')
    nome = input('Digite o seu nome: ').lower()
    parceiro = input('Digite o nome do seu parceiro(a): ').lower()
    placar = 0
    for char in nome:
        if char in parceiro:
            placar += 10
        if char in 'amor':
            placar += 10
    print(f'Seu placar de compatibilidade : {placar}')
    if placar <= 10:
        print('Esqueça essa pessoa! Nunca vai dar certo!')
    elif placar > 10 and placar <= 50:
        print('Seu relacionamento vai ser turbulento!')
    elif placar > 50 and placar <= 70:
        print('Você encontrou uma boa pessoa!')
    elif placar > 70 and placar <= 90:
        print('Seu relacionamento vai ser muito intenso!')
    elif placar > 90:
        print('Você encontrou sua alma gêmea!')
    
if __name__ == '__main__':
    main()
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Doces produzidos
doces = int(input('Digite o número de doces produzidos: '))
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Pacotes disponíveis
pacotes = int(input('Digite a quantidade de pacotes disponíveis: '))
#A variável recebe o resultado da divisão inteira. -> Dividir igualmente os doces nos pacotes
dentro = doces // pacotes
#Imprime na tela quantos doces foram igualmente dividos nos pacotes
print(f'A quantidade de doces dentro dos pacotes será {dentro:0.0f}')

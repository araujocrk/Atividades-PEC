#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Quantidade de anos trabalhados na empresa
tempo = int(input('Quantos anos você trabalha na empresa? '))
#A variável recebe, convertido para real, o valor digitado pelo usuário. valor -> Valor do bônus atual
bonus_ano = float(input('Qual o valor do bônus anual? '))
#A variável recebe o resultado da multiplicação. -> Valor da bonificação
bonificacao = tempo * bonus_ano
#Imprime na tela o valor da bonificação.
print(f'A sua bonificação será de {bonificacao} real(is)')

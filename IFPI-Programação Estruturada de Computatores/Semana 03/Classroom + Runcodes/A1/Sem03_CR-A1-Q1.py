#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Fatias de pizza
pizza = int(input('Quantas fatias de pizza tem? '))
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Pessoas que irão comer a pizza
amigos = int(input('Quantas pessoas irão comer? '))
#A variável recebe o resultado da divisão inteira. -> Quantas fatias irão receber
receber = pizza // amigos
#A variável recebe o resto da divisão inteira. -> Quantas fatias irão sobrar
sobrar = pizza % amigos
#Imprime para o usuário quantos pedaços cada pessoa irá receber e quantos irá sobrar
print(f'Com o total de {pizza} pedaço(s) de pizza para {amigos:0.0f} pessoas,')
print(f'cada um recebe {receber} pedaço(s) e irá sobrar {sobrar}')

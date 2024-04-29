#A variável recebe, convertido para real, o valor digitado pelo usuário. Valor -> Número do dividendo
dividendo = float(input('Insira o valor do dividendo: '))
#A variável recebe, convertido para real, o valor digitado pelo usuário. Valor -> Número do divisor
divisor = float(input('Insira o valor do divisor: '))
#A variável recebe o resultado da divião inteira. 
divisao = dividendo // divisor
#A variável recebe o resto da divisão inteira. 
resto = dividendo % divisor
#Imprime na tela o resultado e o resto da divisão.
print(f'O resultado da divisão é {divisao:.0f} e o resto é {resto:.2f}')


#As variáveis recebem, convertidas para real, os valores digitados pelo usuário
celsius = float(input('Insira a temperatura que deseja em Cº para transformar em Fº: '))
#A variável recebe a transformação de celsius para fahrenheit
fahrenheit = (celsius * (9 / 5)) + 32
#Imprime na tela a temperatura em fahrenheit
print(f'A temperatura é {fahrenheit} Fº')

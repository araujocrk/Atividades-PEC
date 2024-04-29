#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Segundos
segundos = int(input('Insira o número de segundo(s): '))
#A variável recebe o resultado da divisão inteira. -> Transforma os segundos em minutos
minutos = segundos // 60
#A variável recebe o resto da divisão inteira. -> Resto dos segundos que não foram transformados
sobra = segundos % 60
#Imprime na tela quantos minutos e segundos tem a quantidade de segundos inserido pelo usuário
print(f'{segundos} segundo(s) é igual a {minutos} minuto(s) e sobram {sobra} segundo(s).')

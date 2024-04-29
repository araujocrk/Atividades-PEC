#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. Valor -> Quantidade de minutos
minutos = int(input('Insira a quantidade de minuto(s) que você deseja transformar: '))
#A variável recebe o resultado da divisão inteira. -> Transforma os minutos em horas
horas = minutos // 60
#A variável recebe o resto da divisão inteira. -> Quantidade de minutos que não foram transformados em horas
min_resto = minutos % 60
#Imprime na tela quantos minuto(s) equivalem em hora(s) e minuto(s)
print(f'{minutos} minuto(s) equivalem a {horas} hora(s) e {min_resto} minuto(s)')

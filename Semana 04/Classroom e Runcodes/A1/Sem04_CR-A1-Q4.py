#As variáveis recebem, convertidas para inteiro, os valores digitados pelo usuário
hora = int(input('Digite o número de horas: '))
minuto = int(input('Digite o número de minutos: '))
segundo = int(input('Digite o número de segundos: '))
#A variável recebe a transformação de horas para segundos
hora_segundo = hora * 3600
#A variável recebe a transformação de minutos para segundos
minuto_segundo = minuto * 60
#A variável recebe a quantidade total de segundos
seg_passados = hora_segundo + minuto_segundo + segundo
#Imprime na tela a quantidade total de segundos
print(f'Desde a última meia noite se passaram {seg_passados}')

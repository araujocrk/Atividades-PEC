#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Distância até um planeta
distancia = int(input('Qual a distância até o planeta em km? '))
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Velocidade da nave
velo = int(input('E qual a velocidade da sua nave em km/h? '))
#A variável recebe o resultado da divisão. -> Tempo até chegar ao planeta 
tempo = distancia / velo
#A variável recebe o resultado da divisão. -> Transforma o tempo em hora para dia
dias = tempo // 24
#A variável recebe o resto da divisão. -> Resto de horas que não foram transformadas para dia
horas = tempo % 24
#Mostra na tela quantos dias e horas irá demorar o trajeto ao planeta 
print(f'Você irá demorar {dias:0.0f} dia(s) e {horas:0.0f} hora(s) para chegar ao planeta.')           


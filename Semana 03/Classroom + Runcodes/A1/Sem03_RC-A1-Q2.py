distancia = int(input().strip())
velo = int(input().strip())
tempo = distancia / velo
dias = tempo // 24
horas = tempo % 24
print(f'{dias:0.0f} dias e {horas:0.0f} horas')


segundos = int(input().strip())
minutos = segundos // 60
sobra = segundos % 60
print(f'{minutos:0.0f}')
print(f'{sobra:0.0f}')

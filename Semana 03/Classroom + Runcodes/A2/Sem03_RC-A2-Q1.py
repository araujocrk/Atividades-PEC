raio = float(input().strip())
PI = 3.141592
circunferencia = 2 * PI * raio
a_circulo = PI * (raio**2)
a_esfera = 4 * PI * raio ** 2
volume = 4 / 3 * PI * raio ** 3
print(f'{circunferencia:0.6f}')
print(f'{a_circulo:0.6f}')
print(f'{a_esfera:0.6f}')
print(f'{volume:0.6f}')

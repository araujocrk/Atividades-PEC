#A variável recebe, convertido para real, o valor digitado pelo usuário. Valor -> Raio
raio = float(input('Digite o valor do raio: '))
#A "constante" recebe o valor de 3.141592
PI = 3.141592
#A variável recebe o resultado da expressão numérica. -> Tamanho da circunferência 
circunferencia = 2 * PI * raio
#A variável recebe o resultado da expressão numérica. -> Área do círculo
a_circulo = PI * (raio**2)
#A variável recebe o resultado da expressão numérica. -> Área da esfera
a_esfera = 4 * PI * raio ** 2
#A variável recebe o resultado da expressão numérica. -> Volume da esfera
volume = 4 / 3 * PI * raio ** 3
#Imprime na tela os resultados das variáveis "circunferencia", "a_circulo", "a_esfera" e "volume"
print(f'O comprimento da circunferência é aproximadamente {circunferencia:0.2f}')
print(f'A área do círculo é aproximadamente {a_circulo:0.2f}')
print(f'A área da esfera é aproximadamente {a_esfera:0.2f}')
print(f'O volume da esfera é aproximadamente {volume:0.2f}')

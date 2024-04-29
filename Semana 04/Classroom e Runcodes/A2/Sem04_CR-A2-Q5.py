#Imprime na tela a frase abaixo
print('Digite abaixo as 3 notas para receber sua média final')
#As variáveis recebem, convertidas para real, os valores digitados pelo usuário
n1 = float(input())
n2 = float(input())
n3 = float(input())
#A variável recebe o resultado da média ponderada
media = ((n1*2) + (n2*3) + (n3*5)) / 10
#Imprime na tela o resultado da média ponderada
print(f'Sua média final é {media}')

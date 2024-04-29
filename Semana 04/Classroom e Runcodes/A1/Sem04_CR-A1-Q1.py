#As variáveis recebem, convertidas para inteiro, os valores digitados pelo usuário 
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))
#Mostra na tela a formatação da data
print(f'Sua data no Brasil -> {dia}/{mes}/{ano}')
print(f'Sua data nos Estados Unidos -> {mes}/{dia}/{ano}')

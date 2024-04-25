#As variáveis recebem, convertidas para inteiro, os valores digitados pelo usuário
idade_ano = int(input('Qual a sua idade? '))
idade_meses = int(input('E faz quantos meses que você fez aniversário? '))
idade_dias = int(input('E quantos dias? '))
#A variável recebe a transformação de anos de idade para dias
ano_dia = idade_ano *  365
#A variável recebe a transformação de meses de idade para dias 
mes_dia = idade_meses * 30
#A variável recebe a quantidade total de dias de idade
idade_dias_total = ano_dia + mes_dia + idade_dias
#Mostra na tela a quantidade total de dias de vida
print(f'Você tem {idade_dias_total} dias de vida!')

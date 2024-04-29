idade_ano = int(input(''))
idade_meses = int(input(''))
idade_dias = int(input(''))
ano_dia = idade_ano *  365
mes_dia = idade_meses * 30
idade_dias_total = ano_dia + mes_dia + idade_dias
print(f'{idade_dias_total}')

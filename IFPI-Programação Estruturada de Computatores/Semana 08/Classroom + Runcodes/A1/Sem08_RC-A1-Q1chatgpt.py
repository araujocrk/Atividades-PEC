def calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual):
    idade = ano_atual - ano_nascimento

    if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade -= 1

    return idade

# Obtendo a data atual
dia_atual = int(input().strip())
mes_atual = int(input().strip())
ano_atual = int(input().strip())

# Solicitando a data de nascimento da pessoa
dia_nascimento = int(input().strip())
mes_nascimento = int(input().strip())
ano_nascimento = int(input().strip())

# Calculando a idade
idade = calcular_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual)

# Exibindo a idade
print(idade)

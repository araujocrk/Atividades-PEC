#As variáveis recebem, convertidas para real, os valores digitados pelo usuário
altura = float(input('Informe a altura da sua sala em metros: '))
comprimento = float(input('Informe o comprimento da sua sala em metros: '))
largura = float(input('Informe a largura da sua sala em metros: '))
#As variáveis recebem os resultados do volume da sala e área do piso e paredes
a_piso = comprimento * largura
v_sala = altura * comprimento * largura
a_paredes = (2*altura*largura) + (2*altura*comprimento)
#Imprime na tela as variáveis acima
print(f'A área do piso é {a_piso}m²\nO volume da sala é {v_sala}m³\nA área das paredes é {a_paredes}m²')

altura = int(input().strip())
comprimento = int(input().strip())
largura = int(input().strip())
a_piso = comprimento * largura
v_sala = altura * comprimento * largura
a_paredes = 2*altura*largura + 2*altura*comprimento
print(f'{a_piso}\n{v_sala}\n{a_paredes}')

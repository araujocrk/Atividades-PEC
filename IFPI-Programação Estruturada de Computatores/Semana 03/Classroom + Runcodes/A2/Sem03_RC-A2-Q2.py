produto = float(input().strip())
desconto = produto * 0.10
preco_desc = produto - desconto
print(f'{preco_desc:0.2f}')

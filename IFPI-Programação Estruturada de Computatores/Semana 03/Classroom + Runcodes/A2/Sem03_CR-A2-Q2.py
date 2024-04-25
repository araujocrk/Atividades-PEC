#A variável recebe, convertido para real, o valor digitado pelo usuário. Valor -> Preço do produto
produto = float(input('Insira o valor do produto: '))
#A variável recebe o resultado da multiplicação. -> Desconto de 10%
desconto = produto * 0.10
#A variável recebe o resultado da subtração. -> Preço com o desconto de 10%
preco_desc = produto - desconto
#Imprime na tela o preço com desconto.
print(f'O valor do produto com 10% de desconto é {preco_desc:0.2f} reais')

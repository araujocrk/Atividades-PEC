#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Quantidade de Pó de Lua Estelar
lua = int(input('Quantas porções de Pó de Lua Estelar você irá usar na sua poção? '))
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Quantidade de Essência de Dragão
dragao = int(input('E quantas porções de Essência de Dragão? '))
#A variável recebe, convertido para inteiro, o valor digitado pelo usuário. valor -> Quantidade de Lágrima de Fénix
fenix = int(input('Para terminar, quantas porções de Lágrima de Fénix? '))
#A variável recebe o resultado do cálculo matemático. -> Valor total dos itens pedidos pelo usuário
pocao = (lua * 5) + (dragao * 3) + (fenix * 8)
#Mostra na tela quantos ouros o usuário irá gastar para fazer a poção
print(f'Para fazer sua poção, você irá gastar {pocao} moedas de ouro')

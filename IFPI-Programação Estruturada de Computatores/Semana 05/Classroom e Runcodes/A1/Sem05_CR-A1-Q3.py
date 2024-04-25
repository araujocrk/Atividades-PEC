def acrescimo(preco, percentual):
    return preco + ((percentual / 100) * preco)
def desconto(preco, percentual):
    return preco - ((percentual / 100) * preco) 

def main():

    preco = float(input('Digite o preço do produto: '))
    percentual = float(input('Digite o valor percentual: '))

    acrescimo_g = acrescimo(preco, percentual)
    desconto_g = desconto(preco, percentual)

    print(f'O seu produto com {percentual:.0f}% de acréscimo é R${acrescimo_g:.2f}')
    print(f'O seu produto com {percentual:.0f}% de desconto é R${desconto_g:.2f}')

if __name__ == '__main__':
     main()
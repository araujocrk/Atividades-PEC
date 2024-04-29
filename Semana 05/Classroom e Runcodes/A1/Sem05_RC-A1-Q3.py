def acrescimo(preco, percentual):
    return preco + ((percentual / 100) * preco)
def desconto(preco, percentual):
    return preco - ((percentual / 100) * preco) 

def main():

    preco = float(input().strip())
    percentual = float(input().strip())

    acrescimo_g = acrescimo(preco, percentual)
    desconto_g = desconto(preco, percentual)

    print(f'{acrescimo_g:.2f}')
    print(f'{desconto_g:.2f}')

if __name__ == '__main__':
     main()
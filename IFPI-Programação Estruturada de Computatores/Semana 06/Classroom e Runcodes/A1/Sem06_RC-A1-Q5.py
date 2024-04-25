def a_vista(valor_produto):
    preco_desc = valor_produto - (valor_produto * (9/100))
    return f'{preco_desc:.2f}'
def x5(valor_produto):
    parcela = valor_produto / 5
    return f'{parcela:.2f}'
def x10(valor_produto):
    juros = valor_produto * (17/100)
    valor_juros = (valor_produto + juros) / 10
    return f'{valor_juros:.2f}'

def main():
    valor_produto = float(input().strip())

    print(f'{a_vista(valor_produto)}')
    print(f'{x5(valor_produto)}')
    print(f'{x10(valor_produto)}')

if __name__ == '__main__':
     main()
     
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
    valor_produto = float(input('Digite o valor do produto: '))

    print(f'Se você pagar à vista receberá desconto de 9% e pagará R${a_vista(valor_produto)}')
    print(f'Se você dividir em 5 vezes, serão 5 parcelas de R${x5(valor_produto)}')
    print(f'Se você dividir em 10 vezes, serão 10 parcelas de R${x10(valor_produto)}')

if __name__ == '__main__':
     main()
     
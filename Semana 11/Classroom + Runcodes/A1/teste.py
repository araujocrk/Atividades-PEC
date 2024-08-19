def dobro (vl_inicial, tx_juros):
    tempo = 0
    vl_final = vl_inicial
    vl_juros = (vl_final*tx_juros)/100
    while vl_final < (2*vl_inicial):       
         tempo+=1
         vl_final += vl_juros
    return tempo


def main():
    deposito_inicial = float(input('Valor inicial da Poupança: R$ ').strip())
    
    tx_juros_aa = float(input('Taxa de Juros ao Ano (%): ').strip())

    print(f'R${deposito_inicial} rendendo {tx_juros_aa}% ao anp irá dobrar em {dobro(deposito_inicial, tx_juros_aa)} anos.')

if _name_ == '_main_':
    main()
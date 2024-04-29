def valor_frutas(morango, maca):
    if morango <= 5 :
        valor_morango = morango * 2.5
    else: 
        valor_morango = morango * 2.2

    if maca <= 5:
        valor_maca = maca * 1.8
    else:
        valor_maca = maca * 1.5
        
    return valor_morango + valor_maca

def desconto(morango, maca):
    valor = valor_frutas(morango, maca)
    totalkg = morango + maca
    if valor > 25 or totalkg > 8:
        return valor - (valor * 0.1)
    else: 
        return valor
    
def main():
    
    #Entrada
    morango = input('Quantos kg de morango você comprou?\n')
    maca = input('Quantos kg de maçã você comprou?\n')  
    
    #Processamento
    resultado = desconto(morango, maca)
    
    #Saída
    print(f'O valor da sua compra deu R${resultado:.2f}')

if __name__ == '__main__':
    main()
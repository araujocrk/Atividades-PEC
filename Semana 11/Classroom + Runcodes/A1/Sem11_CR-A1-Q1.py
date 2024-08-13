def rendimento_ao_ano(i,t):
    ano = 0
    flag = i*2
    while i < flag:
        i = i + (t / 100 * i)
        ano += 1
    return ano
        
def main():
    inicial = int(input('Qual o depósito inicial? '))
    taxa = int(input('Qual a taxa de juros? '))
    
    resultado = rendimento_ao_ano(inicial, taxa)
    
    print(f'R${inicial:.2f} rendendo {taxa}% ao ano irá dobrar em {resultado} anos.')
    
if __name__ == '__main__':
    main()
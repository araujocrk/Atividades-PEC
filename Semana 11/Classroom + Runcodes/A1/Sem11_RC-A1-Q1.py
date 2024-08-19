def rendimento_ao_ano(i,t):
    ano = 0
    flag = i*2
    while i < flag:
        i = i + (t / 100 * i)
        ano += 1
    return ano
        
def main():
    inicial = float(input().strip())
    taxa = float(input().strip())
    
    resultado = rendimento_ao_ano(inicial, taxa)
    
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()
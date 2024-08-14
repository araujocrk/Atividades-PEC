def main():
    salario = float(input().strip())
    divida = float(input().strip())
    mes = 10
    ano = 2016
    
    while divida <= salario:
        mes += 1
        
        if mes > 12:
            mes = 1
            ano += 1
            
        if mes == 3:
            salario = salario + (5 / 100 * salario)
            
        divida = divida + (15 / 100 * divida)    
    
    print(f'{mes}/{ano}')

if __name__ == '__main__':
    main()
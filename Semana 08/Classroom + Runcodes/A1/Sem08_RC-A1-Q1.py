def anos(dia, mes, ano, dia_n, mes_n, ano_n):
    if dia >= dia_n and mes == mes_n: 
        idade = ano - ano_n
        
    elif dia < dia_n and mes == mes_n:
        idade = ano - ano_n - 1
        
    elif (dia >= dia_n or dia <= dia_n) and mes > mes_n:
        idade = ano - ano_n
        
    elif (dia >= dia_n or dia <= dia_n) and mes < mes_n:     
        idade = ano - ano_n - 1
    
    return idade

def main():
    
    #Entrada
    dia = int(input().strip())
    mes = int(input().strip())
    ano = int(input().strip())
    
    dia_n = int(input().strip())
    mes_n = int(input().strip())
    ano_n = int(input().strip())
    
    #Saída
    print(f'{anos(dia, mes, ano, dia_n, mes_n, ano_n)}')
    
    
    
if __name__ == '__main__':
    main()
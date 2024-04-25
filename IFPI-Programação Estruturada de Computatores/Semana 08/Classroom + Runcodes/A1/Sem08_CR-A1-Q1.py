def anos(dia, mes, ano, dia_n, mes_n, ano_n):
#Se no mês do aniversário, a data atual for igual ou maior que o dia do aniversário, terá completado o ano por meio do cálculo(ano - ano_n)
    if dia >= dia_n and mes == mes_n: 
        idade = ano - ano_n
#Se no mês do aniversário, a data atual for menor que o dia do aniversário, não terá completado o ano diminuindo 1 ano no cálculo(ano - ano_n)        
    elif dia < dia_n and mes == mes_n:
        idade = ano - ano_n - 1
#Se antes, depois ou durante o dia do aniversário, mas depois do mês do aniversário, já completou aniversário por meio do cálculo (ano - ano_n)         
    elif (dia >= dia_n or dia <= dia_n) and mes > mes_n:
        idade = ano - ano_n
#Se antes, depois ou durante o dia do aniversário, mas antes do mês do aniversário, não completou aniversário diminuindo 1 ano (ano - ano_n - 1)        
    elif (dia >= dia_n or dia <= dia_n) and mes < mes_n:     
        idade = ano - ano_n - 1
#Retorna a variável idade    
    return idade

def main():
    
    #Entrada
    dia = int(input('Que dia é hoje?\n'))
    mes = int(input('Em qual mês estamos?\n'))
    ano = int(input('E em qual ano?\n'))
    dia_n = int(input('Que dia você nasceu?\n'))
    mes_n = int(input('De qual mês?\n'))
    ano_n = int(input('Em que ano?\n'))
    
    #Processamento
    idade = anos(dia, mes, ano, dia_n, mes_n, ano_n)
    
    #Saída
    print(f'Sua idade é {idade} anos')
    
    
    
if __name__ == '__main__':
    main()
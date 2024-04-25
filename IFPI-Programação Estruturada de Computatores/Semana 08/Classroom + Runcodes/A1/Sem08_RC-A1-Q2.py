def recente(dia1, mes1, ano1, dia2, mes2, ano2):
    d1 = f'{dia1}/{mes1}/{ano1}'
    d2 = f'{dia2}/{mes2}/{ano2}'
    if ano1 > ano2:
        rec = d1
    elif ano1 < ano2:
        rec = d2      
    elif ano1 == ano2 and mes1 != mes2:
        if mes1 > mes2:
            rec = d1
        else:
            rec = d2
    elif ano1 == ano2 and mes1 == mes2:
        if dia1 > dia2:
            rec = d1
        else:
            rec = d2
    else:
        rec = d1
    return rec
def main():
    
    #Entrada
    dia1 = int(input().strip())
    mes1 = int(input().strip())
    ano1 = int(input().strip())
    
    dia2 = int(input().strip())
    mes2 = int(input().strip())
    ano2 = int(input().strip())
    
    #Processamento
    data_recente = recente(dia1, mes1, ano1, dia2, mes2, ano2)
    
    #Saída
    print(f'{data_recente}')
    
    
    
if __name__ == '__main__':
    main()
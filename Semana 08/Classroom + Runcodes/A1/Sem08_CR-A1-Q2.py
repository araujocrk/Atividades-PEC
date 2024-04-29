def recente(dia1, mes1, ano1, dia2, mes2, ano2):
#A variável d1 recebe a formatação de string da primeira data com as variáveis dia1, mes1 e ano1
    d1 = f'{dia1}/{mes1}/{ano1}'
#A variável d2 recebe a formatação de string da primeira data com as variáveis dia2, mes2 e ano2
    d2 = f'{dia2}/{mes2}/{ano2}'
#Se ano1 for maior que ano2, a variável rec(recente) vai receber a variável d1
    if ano1 > ano2:
        rec = d1
#Se ano1 for menor que ano2, a variável rec(recente) vai receber a variável d2 
    elif ano1 < ano2:
        rec = d2      
#Se ano1 for igual ano2 e mes1 diferente de mes2
    elif ano1 == ano2 and mes1 != mes2:
#E se mes1 for maior que mes2, a variável rec(recente) vai receber a variável d1
        if mes1 > mes2:
            rec = d1
#Se o comentário acima não for verdade, a variável rec(recente) vai receber a variável d2
        else:
            rec = d2
#Se ano1 for igual ano2 e mes1 igual mes2, 
    elif ano1 == ano2 and mes1 == mes2:
#E se dia1 for maior que dia2, a variável rec(recente) vai receber a variável d1
        if dia1 > dia2:
            rec = d1
#Se o comentário acima não for verdade, a variável rec(recente) vai receber a variável d2
        else:
            rec = d2
#Se tudo acima for falso, a variável rec(recente) vai receber a variável d1
    else:
        rec = d1
    return rec
def main():
    
    #Entrada
    dia1 = int(input('Digite um dia: '))
    mes1 = int(input('Digite um mês: '))
    ano1 = int(input('Digite um ano: '))
    
    dia2 = int(input('Digite mais um dia: '))
    mes2 = int(input('Digite mais um mês: '))
    ano2 = int(input('Digite mais um ano: '))
    
    #Processamento
    data_recente = recente(dia1, mes1, ano1, dia2, mes2, ano2)
    
    #Saída
    print(f'Dentre as duas datas, a mais recente é {data_recente}')
    
    
    
if __name__ == '__main__':
    main()
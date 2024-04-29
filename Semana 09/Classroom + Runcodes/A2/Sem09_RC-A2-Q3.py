def data_separada(data):
    a = data % 10000
    data //= 10000
    m = data % 100
    d = data // 100
    return a, m, d

def data_valida(ano, mes, dia):
    bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    if (0 < dia < 32 and mes in [1, 3, 5, 7, 8, 10, 12]) or (0 < dia < 31 and mes in [4, 6, 9, 11]) or (0 < dia < 30 and mes == 2) and bissexto:
        return f'True'
    elif (0 < dia < 32 and mes in [1, 3, 5, 7, 8, 10, 12]) or (0 < dia < 31 and mes in [4, 6, 9, 11]) or (0 < dia < 29 and mes == 2) and bissexto == False:
        return f'True'
    else:
        return f'False'
    
def main():
    
    #Entrada
    data = int(input().strip())
    
    #Processamento
    ano, mes, dia = data_separada(data)
    resultado = data_valida(ano, mes, dia)
    
    #Saída
    print(f'{resultado}')

if __name__ == '__main__':
    main()
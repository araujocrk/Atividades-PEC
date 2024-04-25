def dia_semana(dia):
    if dia == 1:
        return 'domingo'
    elif dia == 2:
        return 'segunda-feira'
    elif dia == 3:
        return 'terça-feira'
    elif dia == 4:
        return 'quarta-feira'
    elif dia == 5:
        return 'quinta-feira'
    elif dia == 6:
        return 'sexta-feira'
    elif dia == 7:
        return 'sábado'
    else:
        return 'valor inválido'

def main():
    
    #Entrada
    print('Digite o dia da semana.')
    dia = int(input('1 - Domingo, 2 - Segunda, ... , 7 - Sábado\n'))
    
    #Processamento
    resultado = dia_semana(dia)
    
    #Saída
    print(f'Seu valor deu: {resultado}')
    
    
    
if __name__ == '__main__':
    main()
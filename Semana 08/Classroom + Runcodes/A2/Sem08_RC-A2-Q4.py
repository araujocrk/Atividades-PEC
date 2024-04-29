def peso(altura, sexo):
    if sexo == '1' or sexo[0].lower() == 'm':
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7
        
def main():
    
    #Entrada
    altura = float(input().strip())
    sexo = input().strip()
    
    #Processamento
    resultado = peso(altura, sexo)

    #Saída
    print(f'{resultado:.2f}')
         
if __name__ == '__main__':
    main()
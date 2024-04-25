# Define a função peso recebendo dois parâmetros
def peso(altura, sexo):
# Se sexo for igual a string 1 ou a primeira letra em minúsculo for igual a string m, retorna altura vezes 72.7 menos 58
    if sexo == '1' or sexo[0].lower() == 'm':
        return (72.7 * altura) - 58
# Senão retorna altura vezes 62.1 - 44.7
    else:
        return (62.1 * altura) - 44.7
        
def main():
    
    #Entrada
    altura = float(input('Qual a sua altura em metros?\n'))
    sexo = input('Digite 1 para sexo masculino e 2 para sexo feminino: ')
    
    #Processamento
    resultado = peso(altura, sexo)

    #Saída
    print(f'O peso ideal para você é {resultado:.2f}')
         
if __name__ == '__main__':
    main()
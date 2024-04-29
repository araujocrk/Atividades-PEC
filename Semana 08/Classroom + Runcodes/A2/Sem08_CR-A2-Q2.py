# Define a função soma recebendo um parâmetro
def soma(n1):
# A variável n recebe a variável n1
    n = n1
# A variável u recebe o resto da divisão n1 por 10
    u = n1 % 10
# A variável n1 recebe o resultado da divisão inteiro n1 por 10
    n1 = n1 // 10
# A variável d recebe o resto da divisão n1 por 10
    d = n1 % 10
# A variável n1 recebe o resultado da divisão inteiro n1 por 10
    n1 = n1 // 10
# A variável c recebe o resto da divisão n1 por 10
    c = n1 % 10
# A variável n1 recebe o resultado da divisão inteiro n1 por 10
    n1 = n1 // 10
# A variável m recebe o resto da divisão n1 por 10
    m = n1 % 10
# A variável n1 recebe o resultado da divisão inteiro n1 por 10
    n1 = n1 // 10
# A variável dm recebe o resto da divisão n1 por 10
    dm = n1 % 10
# A variável n1 recebe o resultado da divisão inteiro n1 por 10
    n1 = n1 // 10
# A variável cm recebe o resto da divisão n1 por 10
    cm = n1 % 10
# Se n for maior que 0 e menor que 100.000, retorna a soma das variáveis u, d, c, m, dm, cm, senão retorna -1
    if 0 < n < 100000:
        return u + d + c + m + dm + cm
    else:
        return -1 

def main():
    
    #Entrada
    n1 = int(input('Digite um número inteiro: '))
    
    #Processamento
    resultado = soma(n1)

    #Saída
# Se n for maior que 0 e menor que 100.000, imprime na tela 'Os dígitos...', senão imprime 'Seu número...'
    if 0 < n1 < 100000:
        print(f'Os dígitos do seu número somados dá {resultado}')
    else:
        print(f'Seu número não está entre 0 e 100.000: {resultado}')
         
    
    
    
if __name__ == '__main__':
    main()
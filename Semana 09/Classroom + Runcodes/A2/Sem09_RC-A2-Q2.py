# Define a função por_extenso recebendo um parâmetro 
def por_extenso(numero):
    # Cria 3 listas, dentro de cada lista tem os números por extenso
    unidades = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    centenas = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    # Cria as variáveis centena, dezena e unidade e resto para separar cada parte do número
    centena = numero // 100
    resto = numero % 100
    dezena = resto // 10
    unidade = resto % 10

    # Cria a variável resultado com uma string vazia
    resultado = ""
    # Se centena for maior que 0
    if centena > 0:
        # A variável resultado recebe a adição de uma str da lista 'centenas' de acordo com a posição do 
        # valor da variável 'centena' 
        resultado += f'{centenas[centena]}'
        # Se centena for maior que 1 (2, 3, 4, ...)
        if centena > 1:
        # A variável resultado recebe a adição da str ' centenas'
            resultado += f' centenas'
        # Se não, centena for (1, 0, ...)
        else:
        # A variável resultado recebe a adição da str ' centena'
            resultado += f' centena'
        # Se dezena for maior que 0 e unidade maior que 0
        if dezena > 0 and unidade > 0:
            # Resultado recebe a adição da str ', '
            resultado += ', '
        # Se o comentário acima for falso e se dezena for maior que 0 e unidade for maior que 0
        elif dezena > 0 or unidade > 0:
        # Resultado recebe a adição da str ' e '
            resultado += ' e '
            
    # Se dezena for maior que 0
    if dezena > 0:
        # A variável resultado recebe a adição de uma str da lista 'dezenas' de acordo com a posição do 
        # valor da variável 'dezena' 
        resultado += f'{dezenas[dezena]}'
        # Se dezena for maior que 1 (2, 3, 4, ...)
        if dezena > 1:
        # A variável resultado recebe a adição da str ' dezenas'
            resultado += ' dezenas'
        # Se não, dezena for (1, 0, ...)
        else:
        # A variável resultado recebe a adição da str ' dezena'
            resultado += ' dezena'
        # Se unidade for maior que 0
        if unidade > 0:
        # Resultado recebe a adição da str ' e '  
            resultado += ' e '
    
    # Se unidade for maior que 0        
    if unidade > 0:
        # A variável resultado recebe a adição de uma str da lista 'unidades' de acordo com a posição do 
        # valor da variável 'unidade' 
        resultado += f'{unidades[unidade]}'
        # Se unidade for maior que 1 (2, 3, 4, ...)
        if unidade > 1:
        # A variável resultado recebe a adição da str ' unidades'    
            resultado += f' unidades'
        # Se não, dezena for (1, 0, ...)
        else:
        # A variável resultado recebe a adição da str ' unidade'    
            resultado += ' unidade'
    # A função retorna a variável resultado
    return resultado

def main():
    # Entrada de dados
    numero = int(input().strip())
    print(f'{por_extenso(numero)}.')


if __name__ == "__main__":
    main()

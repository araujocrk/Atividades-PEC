# Define a função mf recebendo quatro parâmetros
def mf(n1, n2, n3, me):
# Retorna o cálculo com as variáveis n1, n2, n3, me.  (n1 + (n2 * 2) + (n3 * 3) + me) / 7
    return (n1 + (n2 * 2) + (n3 * 3) + me) / 7
# Define a função conceito recebendo quatro parâmetros
def conceito(n1, n2, n3, me):
# A variável medfin recebe o retorno da função mf(n1, n2, n3, me)
    medfin = mf(n1, n2, n3, me)
# A constante A recebe a variável medfin maior ou igual que 9 em valor booleano
    A = medfin >= 9
# A constante B recebe a variável medfin maior ou igual que 7.5 e menor que 9 em valor booleano
    B = 7.5 <= medfin < 9
# A constante C recebe a variável medfin maior ou igual que 6 e menor que 7.5 em valor booleano
    C = 6 <= medfin < 7.5
# A constante D recebe a variável medfin maior ou igual que 4 e menor que 6 em valor booleano
    D = 4 <= medfin < 6
# A constante E recebe a variável medfin menor que 4 em valor booleano
    E = medfin < 4
# Se as constantes A, B e C forem verdadeiras, retorna a formatação de string
    if A and B and C:
        return f'Pelos conceitos A, B e C você foi Aprovado'
# Se o comentário acima for falso e as constantes A e B forem verdadeiras, retorna a formatação de string
    elif A and B:
        return f'Pelos conceitos A e B você foi Aprovado'
# Se o comentário acima for falso e as constantes A e C forem verdadeiras, retorna a formatação de string
    elif A and C:
        return f'Pelos conceitos A e C você foi Aprovado'
# Se o comentário acima for falso e as constantes B e C forem verdadeiras, retorna a formatação de string
    elif B and C:
        return f'Pelos conceitos B e C você foi Aprovado'
# Se o comentário acima for falso e a constante A for verdadeira, retorna a formatação de string
    elif A:
        return f'Pelos conceito A você foi Aprovado'
# Se o comentário acima for falso e a constante B for verdadeira, retorna a formatação de string
    elif B:
        return f'Pelos conceito B você foi Aprovado'
# Se o comentário acima for falso e a constante C for verdadeira, retorna a formatação de string
    elif C:
        return f'Pelos conceito C você foi Aprovado'
# Se o comentário acima for falso e as constantes D e E forem verdadeiras, retorna a formatação de string
    elif D and E:
        return f'Pelos conceitos D e E você foi Reprovado'
# Se o comentário acima for falso e a constante D for verdadeira, retorna a formatação de string
    elif D:
        return f'Pelo conceito D você foi Reprovado'
# Se o comentário acima for falso e a constante E for verdadeira, retorna a formatação de string
    elif E:
        return f'Pelo conceito E você foi Reprovado'
        
def main():
    
    #Entrada
    matricula = input('Insira sua matrícula: ')
    n1 = float(input('Insira sua 1ª nota: '))
    n2 = float(input('Insira sua 2ª nota: '))
    n3 = float(input('Insira sua 3ª nota: '))
    me = float(input('Digite sua média obtida dos exercícios: '))
    
    #Processamento
    media_final = mf(n1, n2, n3, me)
    resultado = conceito(n1, n2, n3, me)

    #Saída
    print(f'Matrícula: {matricula} \nMédia Final: {media_final:.2f} \nResultado: {resultado}')
         
if __name__ == '__main__':
    main()
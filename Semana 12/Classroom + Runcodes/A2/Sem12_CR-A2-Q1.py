# Função que irá calcular o fatorial do número lido
def fatorial(n):
    # Se o número lido for igual a 0, então o fatorial desse número é 1
    if n == 0:
        return 1
    # Se o número lido não for igual a 0 e ser maior que 1
    elif n > 0:
        # Inicializa o acumulador fatorial
        fatorial = 1
        # Estrutura de repetição determinado começando com 1 e terminando no número lido
        for c in range(1, n + 1):
            # Até que o loop chegue no número lido, fatorial vai multiplicar pelo contador
            fatorial *= c
        return fatorial
def main():
   
   # Entrada de dados
   num = int(input('Digite o número para o cálculo fatorial: '))
   
   # Processamento
   resultado = fatorial(num)
   
   # Saída de dados
   print(f'O fatorial do número {num} é {resultado}')
       
if __name__ == "__main__":
    main()
# Função que irá separar 8 vezes o ultimo dígito e somar eles.
def numero_da_sorte(dn):
    # Inicializa o acumulador para somar os dígitos
    num_sorte = 0
    # O loop irá repetir 8 vezes e ... 
    for c in range(8):
        # a variável dig receberá o ultimo digito da data de nascimento...
        dig = dn % 10
        # a variável dn perderá o ultimo digito
        dn //= 10
        # e o acumulador num_sorte somará os valores de dig
        num_sorte += dig
    return num_sorte 

def main():
    # Entrada de dados
   data_nasc = int(input('Digite sua data de nascimento no formato DDMMAAAA para saber seu número da sorte: '))
   
   # Processamento
   resultado = numero_da_sorte(data_nasc)
   
   # Saída de dados
   print(f'Seu número da sorte é {resultado}')

if __name__ == "__main__":
    main()
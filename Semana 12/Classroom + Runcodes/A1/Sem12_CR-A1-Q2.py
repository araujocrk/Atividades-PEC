# Função que irá calcular quando terá dinheiro para comprar o carro
def comprar_carro(car):
    # Inicializa o contador de meses até conseguir comprar o carro
    mes = 0
    # Inicializa o valor inicial da poupança
    poupanca = 10000
    # Constante que possui o valor de rendimento da poupança ao mês
    RENDE_AM = 0.7 / 100
    # Constante que possui o valor da taxa que aumenta o preço do carro ao mês
    TAXA_AM = 0.4 / 100
    # Enquanto o valor do carro ser maior que o da poupança, o loop continuará
    while car >= poupanca:
        poupanca += poupanca * RENDE_AM
        car += car * TAXA_AM
        mes += 1
    return mes

def main():
    
    # Entrada de dados
    carro = float(input('Digite o valor atual do carro que deseja comprar: '))
    
    # Processamento
    resultado = comprar_carro(carro)
    
    # Saída de dados
    print(f'Com o dinheiro da poupança, você conseguirá comprar seu carro em {resultado} meses')
    
    
if __name__ == "__main__":
    main()
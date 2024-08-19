# Função para inverter o número lido
def inverter(n):
    inv = 0
    # Estrutura de repetição que enquanto o numero lido for maior que 0, será retirado o ultimo dígito e colocado na variavel inv
    while n > 0:
        dig = n % 10
        inv = inv * 10 + dig
        n //= 10
    return inv
    
def main():
    # Entrada de dados
    numero = int(input('Digite um número inteiro para inverter: '))
    
    # Processamento
    num_inv = inverter(numero)  
    
    # Saída de dados
    print(f'Seu número invertido fica assim: {num_inv}')       

if __name__ == '__main__':
    main()
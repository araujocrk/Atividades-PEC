# Função para calcular quando a lebre alncançar a tartaruga
def alcancar(tartaruga):
    # Inicializa o contador de minutos até a lebre chegar na tartaruga do zero
    minutos = 0
    # Inicializa o contador de metros/min em que a lebre corre
    lebre = 0
    # Enquanto a tartaruga estiver na frente da lebre, o loop continuará 
    while tartaruga > lebre:
        lebre += 10
        tartaruga += 1
        minutos += 1
    return minutos
def main():
    
    # Entrada de dados
    tartaruga = int(input().strip())
    
    # Processamento
    resultado = alcancar(tartaruga)
    
    # Saída de dados
    print(f'{resultado}')
    
if __name__ == "__main__":
    main()
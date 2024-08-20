def main():
    
    ano = 0
    tx_n_aa_A = 2 / 100
    tx_n_aa_B = 3 / 100
    
    pA = int(input('Digite quantas pessoas tem no país A (maior população) : '))
    pB = int(input('Digite quantas pessoas tem no país B (menor população) : '))
    
    while pB > pA:
        pA += pA * tx_n_aa_A
        pB += pB * tx_n_aa_B
        ano += 1
    
    print(f'A população do país A irá ultrapassar a população do país B em {ano} anos')
        
    
    
if __name__ == "__main__":
    main()
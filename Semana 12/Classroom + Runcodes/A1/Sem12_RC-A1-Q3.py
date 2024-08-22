def main():
    ano = 0
    tx_n_aa_A = 2 / 100
    tx_n_aa_B = 3 / 100
    
    pA = aux1 = int(input().strip())
    pB = aux2 = int(input().strip())
    
    if pA > pB:
        while pA > pB:
            pA += pA * tx_n_aa_A
            pB += pB * tx_n_aa_B
            ano += 1
    else:
        while pB > pA:
            pA += pA * tx_n_aa_B
            pB += pB * tx_n_aa_A
            ano += 1

    print(f'{ano}')
        
if __name__ == "__main__":
    main()
def main():
    
    ano = 0
    tx_n_aa_A = 2 / 100
    tx_n_aa_B = 3 / 100
    
    p1 = int(input().strip())
    p2 = int(input().strip())
    
    if p1 > p2:
        pA = p1
        pB = p2
    else:
        pA = p2
        pB = p1
    
    while pA > pB:
        pA += pA * tx_n_aa_A
        pB += pB * tx_n_aa_B
        ano += 1
    
    print(f'{ano}')
        
    
    
if __name__ == "__main__":
    main()
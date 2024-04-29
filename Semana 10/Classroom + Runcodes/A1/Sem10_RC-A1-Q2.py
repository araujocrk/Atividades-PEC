def qtd_par_impar(qtd):
    impar = 0
    par = 0
    for n in range(qtd):
        num = int(input().strip())
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
            
    return par, impar        

def main():
    res_par, res_impar = qtd_par_impar(100)
    
    print(f'{res_par}')
    print(f'{res_impar}')

if __name__ == '__main__':
    main()
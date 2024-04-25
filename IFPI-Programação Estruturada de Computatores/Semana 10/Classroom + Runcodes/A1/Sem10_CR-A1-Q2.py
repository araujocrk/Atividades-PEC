def qtd_par_impar(qtd):
    impar = 0
    par = 0
    for n in range(qtd):
        num = int(input('Digite um números inteiro positivo: '))
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
            
    return par, impar        

def main():
    res_par, res_impar = qtd_par_impar(100)
    
    print(f'No seu conjunto de números tem {res_par} pares e {res_impar} ímpares.')
if __name__ == '__main__':
    main()
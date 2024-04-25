def eh_impar(numero):
    return numero % 2 == 1
def unidade(numero):
    u = numero % 10
    return eh_impar(u)
def dezena(numero):
    numero = numero // 10 
    d = numero % 10
    return eh_impar(d)
def centena(numero):
    u = numero % 10
    numero = numero // 10
    d = numero % 10
    numero = numero // 10
    c = numero % 10
    return eh_impar(c)

def main():

    n1 = int(input('Digite um número entre 10 e 99: '))
    
    if 10 <= n1 <= 99:
        if unidade(n1) and dezena(n1):
            print(f'Os dois dígitos são ímpares.')
        elif unidade(n1) or dezena(n1):
            print(f'Apenas um dígito é ímpar.')
        else:
            print(f'Nenhum dígito é ímpar.')
    elif 0 <= n1 <= 9:
        if unidade(n1):
            print('Um dígito é ímpar.')
        else:
            print('Nenhum dígito é ímpar.')
    elif 100 <= n1 <= 999:
        if unidade(n1) and dezena(n1) and centena(n1):
            print(f'Os três dígitos são ímpares.')
        elif unidade(n1) and dezena(n1) or unidade(n1) and centena(n1) or dezena(n1) and centena(n1):
            print(f'Os dois dígitos são ímpares.')
        elif unidade(n1) or dezena(n1) or centena(n1):
            print(f'Apenas um dígito é ímpar.')
        else:
            print(f'Nenhum dígito é ímpar.')



         



if __name__ == '__main__':
     main()
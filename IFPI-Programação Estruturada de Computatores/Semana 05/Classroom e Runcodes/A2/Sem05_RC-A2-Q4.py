def l_n(caractere):
    letra_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ0123456789'
    return caractere in letra_num

def main():
    caractere = input().strip()

    fun_l_n = l_n(caractere)

    print(f'{fun_l_n}')

if __name__ == '__main__':
     main()
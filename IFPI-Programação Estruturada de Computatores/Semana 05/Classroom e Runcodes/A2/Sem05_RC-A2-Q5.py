def simbolo(caractere):
    letra_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZçÇ0123456789'
    return caractere not in letra_num

def main():
    caractere = input().strip()

    fun_simbolos = simbolo(caractere)

    print(f'{fun_simbolos}')

if __name__ == '__main__':
     main()
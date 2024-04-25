def upper(cor):
    return cor[0].upper()


def main():
    cor = input().strip()

    if upper(cor) == 'V':
        print('Siga')
    elif upper(cor) == 'A':
        print('Atenção')
    elif upper(cor) == 'E':
        print('Pare')
 

if __name__ == '__main__':
     main()
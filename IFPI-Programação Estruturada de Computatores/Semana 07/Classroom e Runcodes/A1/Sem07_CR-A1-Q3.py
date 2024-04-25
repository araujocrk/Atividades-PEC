def upper(cor):
    return cor[0].upper()


def main():
    cor = input('Qual a cor do semáforo? (V - verde, A - amarelo e E - vermelho)\n')

    if upper(cor) == 'V':
        print('Siga!')
    elif upper(cor) == 'A':
        print('Atenção!')
    elif upper(cor) == 'E':
        print('Pare!')
    else:
        print('Erro na entrada de dados! (Tente novamente usando V, A ou E)')    

if __name__ == '__main__':
     main()
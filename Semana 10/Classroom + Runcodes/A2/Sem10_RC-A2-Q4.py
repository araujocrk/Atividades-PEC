def repetir_musica(ini,fim,intv):
    for num in range(ini, fim, intv):
        print((str(num)) + ' ' + 'bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')

def main():
    repetir_musica(99, 0, -11)
    print(f'Sem erros no software! Está estabilizado!')
    
if __name__ == '__main__':
    main()
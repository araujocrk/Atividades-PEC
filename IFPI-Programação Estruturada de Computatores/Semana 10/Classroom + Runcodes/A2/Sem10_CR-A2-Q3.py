def repetir_musica(ini, fim, intv):
    for num in range(ini, fim, intv):
        print((str(num)) + ' ' + 'bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')

def main():
    repetir_musica(99, 251, 7)
    print(f'Vamos fazer mais um café!')
    
if __name__ == '__main__':
    main()
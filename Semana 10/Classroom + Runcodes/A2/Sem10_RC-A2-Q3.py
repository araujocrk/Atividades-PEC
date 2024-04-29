def repetir_musica(i,f):
    for num in range(i, f, 7):
        print((str(num)) + ' ' + 'bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')

def main():
    repetir_musica(99, 251)
    print(f'Vamos fazer mais um café!')
    
if __name__ == '__main__':
    main()
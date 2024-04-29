def repetir_musica(i, f, intv):
    for num in range(i, f, intv):
        print((str(num)) + ' ' + 'bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
    print(f'Vamos fazer mais um café!')
def main():
    repetir_musica(99, 251, 7)
    
if __name__ == '__main__':
    main()

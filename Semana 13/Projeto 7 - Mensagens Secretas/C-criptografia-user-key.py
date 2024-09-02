def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    chave = int(input('Por favor, entre com uma chave para criptografar: '))
    letra = input('Por favor, entre com uma letra para criptografar: ').lower()
    
    posicao = alfabeto.find(letra)
    
    novaPosicao = (posicao + chave) % 26
    
    letraCriptografada = alfabeto[novaPosicao]
    
    print(f'Sua letra criptografada é: {letraCriptografada}')
    
if __name__ == '__main__':
    main()
def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    chave = 3
    
    letra = input('Por favor, entre com uma letra para criptografar: ').lower()
    
    posicao = alfabeto.find(letra)
    
    novaPosicao = (posicao + chave) % 26
    
    letraCriptografada = alfabeto[novaPosicao]
    
    print(f'Sua letra criptografada é: {letraCriptografada}')
    
if __name__ == '__main__':
    main()
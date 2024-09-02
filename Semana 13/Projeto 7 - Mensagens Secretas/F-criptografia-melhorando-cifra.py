def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    mensagem = input('Por favor, entre com a mensagem a ser criptografada: ').lower()
    
    mensagemCriptografada = ''
    
    chave = input('Por favor, entre com a chave: ')
    chave = int(chave)
    
    for char in mensagem:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            novaPosicao = (posicao + chave) % 26
            mensagemCriptografada += alfabeto[novaPosicao]
            chave += 1
        else:
            mensagemCriptografada += char
        
    print(f'Sua mensagem criptografada é: {mensagemCriptografada}')
if __name__ == '__main__':
    main()
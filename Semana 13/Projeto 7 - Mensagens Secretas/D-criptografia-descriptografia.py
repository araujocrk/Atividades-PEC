def criptografar(c, l, alfabeto):
    posicao = alfabeto.find(l)
    novaPosicao = (posicao + c) % 26
    letraCriptografada = alfabeto[novaPosicao]
    return letraCriptografada
    
def descriptografar(c, frase, alfabeto):
    fraseDescriptografada = ''
    for i in range(len(frase)):
        posicao = alfabeto.find(frase[i])
        novaPosicao = (posicao - c) % 26
        letraDescriptografada = alfabeto[novaPosicao]
        fraseDescriptografada += letraDescriptografada
    return fraseDescriptografada
        
def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    print(criptografar(7, 'd', alfabeto))
    print(criptografar(4, 'x', alfabeto))
    print(descriptografar(12, 'omqemd', alfabeto))
    
if __name__ == '__main__':
    main()
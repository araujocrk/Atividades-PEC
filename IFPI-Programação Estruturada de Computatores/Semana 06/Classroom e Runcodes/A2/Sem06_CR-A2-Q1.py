def length(frase):
    return len(frase)

def main():
    frase = input('Digite uma frase: ').strip()

    print(f'A sua frase tem {length(frase)} caracteres!')

if __name__ == '__main__':
     main()
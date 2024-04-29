def media(t):
    media = t / 100
    return media

def main():
    total = 0
    for n in range(100):
        num = int(input('Digite um número inteiro: '))
        total += num
    
    resultado = media(total)
    
    print(f'A média dos seus números é {resultado:.2f}')
if __name__ == '__main__':
    main()
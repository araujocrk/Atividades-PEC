def media(t):
    media = t / 100
    return media

def main():
    total = 0
    for n in range(100):
        num = int(input().strip())
        total += num
    
    resultado = media(total)
    
    print(f'{resultado:.2f}')
    
if __name__ == '__main__':
    main()
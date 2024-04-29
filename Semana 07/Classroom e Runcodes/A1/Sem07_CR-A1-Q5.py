def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def main():
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    n3 = float(input('Digite a 3ª nota: '))

    if n3 > 8:
        if media(n1, n2, n3) + 1 <= 10:
            print(f'Sua média é {media(n1, n2, n3) + 1:.2f}')
        else:
            print(f'Sua média é 10')
    elif n3 <= 8:
        print(f'Sua média é {media(n1, n2, n3):.2f}')


if __name__ == '__main__':
     main()
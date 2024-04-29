def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def main():
    n1 = float(input().strip())
    n2 = float(input().strip())
    n3 = float(input().strip())

    if n3 > 8:
        if media(n1, n2, n3) + 1 <= 10:
            print(f'{media(n1, n2, n3) + 1:.2f}')
        else:
            print(f'10')
    elif n3 <= 8:
        print(f'{int((media(n1, n2, n3) * 100)) / 100:0.2f}')


if __name__ == '__main__':
     main()
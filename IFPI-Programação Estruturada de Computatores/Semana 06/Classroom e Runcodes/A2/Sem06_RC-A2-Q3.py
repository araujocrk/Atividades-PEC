def total(maca, banana):
    preco_total = (maca*3) + (banana*2)
    return f'{preco_total:.2f}'

def main():
    maca = float(input().strip())
    banana = float(input().strip())

    print(f'{total(maca, banana)}')

if __name__ == '__main__':
     main()
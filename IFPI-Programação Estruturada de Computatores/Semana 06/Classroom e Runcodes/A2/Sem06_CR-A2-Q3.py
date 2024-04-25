def total(maca, banana):
    preco_total = (maca*3) + (banana*2)
    return f'{preco_total:.2f}'

def main():
    maca = float(input('Quanto custa a maçã? '))
    banana = float(input('Quanto custa a banana? '))

    print(f'O total da minha compra é R${total(maca, banana)}')

if __name__ == '__main__':
     main()
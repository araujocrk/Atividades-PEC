def cel_fah(celsius):
    fahrenheit =  (celsius*(9/5)) + 32
    return f'{fahrenheit:.2f}'

def main():
    celsius = float(input('Qual a temperatura em °C? '))

    print(f'{celsius:.2f}°C é igual a {cel_fah(celsius)}°F')

if __name__ == '__main__':
     main()
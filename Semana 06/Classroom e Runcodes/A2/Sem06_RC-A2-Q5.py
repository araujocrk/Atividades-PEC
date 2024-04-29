def cel_fah(celsius):
    fahrenheit =  (celsius*(9/5)) + 32
    return f'{fahrenheit:.2f}'

def main():
    celsius = float(input().strip())

    print(f'{cel_fah(celsius)}')

if __name__ == '__main__':
     main()
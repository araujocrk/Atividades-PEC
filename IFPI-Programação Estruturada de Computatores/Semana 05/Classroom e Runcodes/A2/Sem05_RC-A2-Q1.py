def vogal(caractere):
    vogais = 'aeiouAEIOU'
    return caractere in vogais

def main():
    caractere = input().strip()

    pri_carac = vogal(caractere)

    print(f'{pri_carac}')

if __name__ == '__main__':
     main()
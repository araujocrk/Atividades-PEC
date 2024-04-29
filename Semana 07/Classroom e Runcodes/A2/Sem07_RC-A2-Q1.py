def length(nome, civil, conjuge):
    if civil == '1' or civil[0].upper() == 'C':
        return len(nome) + len(conjuge)
    else:
        return len(nome)


def main():
    nome = input().strip()
    civil = input().strip()

    if civil == '1' or civil[0].upper() == 'C':
        conjuge = input().strip()
        print(f'{length(nome, civil, conjuge)}')
    else:
        conjuge = 0
        print(f'{length(nome, civil, conjuge)}')

if __name__ == '__main__':
     main()
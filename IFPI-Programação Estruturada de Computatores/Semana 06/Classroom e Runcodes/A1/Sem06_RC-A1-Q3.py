def evento(segundo):
    hora = segundo // 3600
    segundo = segundo % 3600
    min = segundo // 60
    sec = segundo % 60
    retorno = (f'{hora}:{min}:{sec}')
    return retorno

def main():
    segundos = int(input().strip())

    print(f'{evento(segundos)}')

if __name__ == '__main__':
     main()
     
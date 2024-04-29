def evento(segundo):
    hora = segundo // 3600
    segundo = segundo % 3600
    min = segundo // 60
    sec = segundo % 60
    retorno = (f'{hora} hora(s), {min} minuto(s) e {sec} segundo(s)')
    return retorno

def main():
    segundos = int(input('Quanto tempo demorou em segundos o evento na fábrica? '))

    print(f'{segundos} segundo(s) demorou {evento(segundos)}')

if __name__ == '__main__':
     main()
     
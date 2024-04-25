def m_h(min):
    return (min // 60)
def m_resto(min):
    return (min % 60)         

def main():

    minutos = int(input('Digite uma quantidade de minutos '))

    horas = m_h(minutos)
    resto = m_resto(minutos)

    print(f'{minutos} minutos é equivalente à {horas} horas e {resto} minutos')

if __name__ == '__main__':
     main()
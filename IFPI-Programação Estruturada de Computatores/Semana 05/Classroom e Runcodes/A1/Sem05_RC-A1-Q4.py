def m_h(min):
    return (min // 60)
def m_resto(min):
    return (min % 60)         

def main():

    minutos = int(input().strip())

    horas = m_h(minutos)
    resto = m_resto(minutos)

    print(f'{horas}:{resto}')

if __name__ == '__main__':
     main()
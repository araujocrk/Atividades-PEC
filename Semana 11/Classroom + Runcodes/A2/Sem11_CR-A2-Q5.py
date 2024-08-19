def main():
    while True:
        nota = float(input('Digite sua nota: '))
        if 0 <= nota <= 10: break
        else:
            print(f'Nota inválida.')
            
    if nota >= 8.5:
        conceito = "A"
    elif nota >= 7.0:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 4.0:
        conceito = "D"
    else:
        conceito = "E"
        
    print(f'O conceito da sua nota é {conceito}')
            
if __name__ == '__main__':
    main()
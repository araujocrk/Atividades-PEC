#função para receber as médias de temperatura por mes em C, F e K
def preencherTemperaturas(qtd):
    temperaturas = []
    MESES = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    for i in range(qtd):
        grau = float(input(f'Insira a média da temperatura de {MESES[i]}: '))
        escala = input(f'Insira a escala da temperatura de {MESES[i]}: ').upper()[0]
        temperaturas.append((grau, escala))
    return temperaturas

#função que converte C para K
def celsiusToKelvin(celsius):
    return celsius + 273.15

#função que converte F para K
def fahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * (5/9) + 273.15

#função para calcular a média anual em K
def mediaAnual(temperaturas):
    soma = 0
    for g, e in temperaturas:
        if e == 'C':
            soma += celsiusToKelvin(g)
        elif e == 'F':
            soma += fahrenheitToKelvin(g)
        else:
            soma += g
    return round(soma / len(temperaturas), 2)

#função que cria uma lista com as temperaturas em K
def temperaturasKelvin(temperaturas):
    tempKelvin = []
    for g, e in temperaturas:
        if e == 'C':
            tempKelvin.append(celsiusToKelvin(g))
        elif e == 'F':
            tempKelvin.append(fahrenheitToKelvin(g))
        else:
            tempKelvin.append(g)
    return tempKelvin

#função para informar os valores que são maiores que a média anual
def acimaMediaAnual(tempKelvin, media):
    MESES = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    for i in range(len(tempKelvin)):
        if tempKelvin[i] > media:
            print(f'{MESES[i]}: {round(tempKelvin[i], 2)}K')

def main():
    temperaturas = preencherTemperaturas(12)
    media = mediaAnual(temperaturas)
    print(f'TEMPERATURA MÉDIA ANUAL')
    print(f'{media}K')
    print(f'TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    acimaMediaAnual(temperaturasKelvin(temperaturas), media)

if __name__ == '__main__':
    main()
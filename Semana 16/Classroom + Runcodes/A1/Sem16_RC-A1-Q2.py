#função para receber as médias de temperatura por mes em C, F e K
def preencherTemperaturas(qtd):
    temperaturas = []
    for i in range(qtd):
        grau = float(input().strip())
        escala = input().strip().upper()[0]
        temperaturas.append((grau, escala))
    return temperaturas

#função que converte C para K
def celsiusToKelvin(celsius):
    return celsius + 273.15

#função que converte F para K
def fahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * (5/9) + 273.15

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

#função para calcular a média anual em K
def mediaAnual(tempKelvin):
    soma = 0
    for e in tempKelvin:
        soma += e
    return round(soma / len(tempKelvin), 2)

#função para informar os valores que são maiores que a média anual
def acimaMediaAnual(tempKelvin, media):
    MESES = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    for i in range(len(tempKelvin)):
        if tempKelvin[i] > media:
            print(f'{MESES[i]}: {round(tempKelvin[i], 2)}K')

def main():
    temperaturas = preencherTemperaturas(12)
    media = mediaAnual(temperaturasKelvin(temperaturas))
    print(f'TEMPERATURA MÉDIA ANUAL')
    print(f'{media}K')
    print(f'TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    acimaMediaAnual(temperaturasKelvin(temperaturas), media)

if __name__ == '__main__':
    main()
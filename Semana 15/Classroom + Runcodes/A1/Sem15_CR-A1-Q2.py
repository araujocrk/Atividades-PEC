def fahrenheitToCelsius(f):
    return (f - 32) * (5/9)

def celsiusToFahrenheit(c):
    return (c * (9/5)) + 32

def somarTemperatura(g1, e1, g2, e2):
    if e1 == 'C' and e2 == 'C':
        return round(g1 + g2, 4), 'C'
    elif e1 == 'F' and e2 == 'F':
        return round(g1 + g2, 4), 'F'
    
    elif e1 == 'C' and e2 == 'F':
        g1 = celsiusToFahrenheit(g1)
        return round(g1 + g2, 4), 'F'
    
    elif e1 == 'F' and e2 == 'C':
        g1 = fahrenheitToCelsius(g1)
        return round(g1 + g2, 4), 'C'
        
def main():
    grau1 = float(input('Insira o grau da primeira temperatura: '))
    escala1 = input('Insira a escala da primeira temperatura: ').upper()[0]
    grau2 = float(input('Insira o grau da segunda temperatura: '))
    escala2 = input('Insira a escala da segunda temperatura: ').upper()[0]    
    
    somaTemp = somarTemperatura(grau1, escala1, grau2, escala2)
    print(f'A soma das temperaturas é {somaTemp}')
    
if __name__ == "__main__":
    main()
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
    grau1 = float(input().strip())
    escala1 = input().strip().upper()[0]
    grau2 = float(input().strip())
    escala2 = input().strip().upper()[0]    
    
    somaTemp = somarTemperatura(grau1, escala1, grau2, escala2)
    print(f'{somaTemp}')
    
if __name__ == "__main__":
    main()
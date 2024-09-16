def fahrenheitToCelsius(f):
    return (f - 32) * (5/9)

def maiorTemperatura(t1, t2):
    g1, e1 = t1
    g2, e2 = t2
    
    if e1 == 'C' and e2 == 'F':
        g2 = fahrenheitToCelsius(g2)
    elif e1 == 'F' and e2 == 'C':
        g1 = fahrenheitToCelsius(g1)
    if g1 > g2:
        return t1
    else:
        return t2


def main():
    grau1 = float(input().strip())
    escala1 = input().strip().upper()[0]
    grau2 = float(input().strip())
    escala2 = input().strip().upper()[0]
    
    temperatura1 = (grau1, escala1)
    temperatura2 = grau2, escala2
    
    maiorTemp = maiorTemperatura(temperatura1, temperatura2)
    print(f'{maiorTemp}')
    
if __name__ == "__main__":
    main()
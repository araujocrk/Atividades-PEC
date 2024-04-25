def area(lado_l):
    return (lado_l) ** 2
def peri(lado_l):
    return lado_l * 4
def main():
    lado_g = float(input().strip())

    a_quadrado = area(lado_g)
    p_quadrado = peri(lado_g)
    print(f'{a_quadrado:10.4f}')
    print(f'{p_quadrado:10.4f}')
if __name__ == '__main__':
     main()
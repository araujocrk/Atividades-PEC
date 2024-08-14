def inverter(n):
    inv = 0
    while n > 0:
        dec = n % 10
        inv = inv * 10 + dec
        n //= 10
    return inv
    
def main():
    numero = int(input().strip())
    
    num_inv = inverter(numero)  
    
    print(f'{num_inv}')       

if __name__ == '__main__':
    main()
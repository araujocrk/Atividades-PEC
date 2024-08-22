def numero_da_sorte(dn):
    num_sorte = 0
    for c in range(8):
        dig = dn % 10
        dn //= 10
        num_sorte += dig
    return num_sorte 

def main():
   data_nasc = int(input().strip())
   
   
   resultado = numero_da_sorte(data_nasc)
   
   print(f'{resultado}')

if __name__ == "__main__":
    main()
def fatorial(n):
    if n == 0:
        return 1
    elif n > 0:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial
def main():
   
   num = int(input().strip())
   
   resultado = fatorial(num)
   
   print(f'{resultado}')
       
if __name__ == "__main__":
    main()
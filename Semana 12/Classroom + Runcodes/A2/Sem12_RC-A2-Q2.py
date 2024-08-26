def main():
    termo1 = 0
    termo2 = 1
   
    num = int(input().strip())
   
    print(f'{termo1}, {termo2}', end=', ')
   
    for c in range(2, num - 1):
       prox_termo = termo1 + termo2
       print(f'{prox_termo}', end=', ')
       termo1 = termo2
       termo2 = prox_termo
       
    print(f'{termo1 + termo2}')
       
if __name__ == "__main__":
    main()
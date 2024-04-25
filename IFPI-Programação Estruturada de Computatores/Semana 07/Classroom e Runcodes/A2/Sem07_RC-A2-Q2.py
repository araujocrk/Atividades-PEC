def udc(n1):
    if 1000 <= n1 <= 9999:
        u = n1 % 10
        n1 = n1 // 10
        d = n1 % 10
        n1 = n1 // 10
        c = n1 % 10
        n1 = n1 // 10
        m = n1 % 10
        n1 = 0
    if 100 <= n1 <= 999:
        u = n1 % 10
        n1 = n1 // 10
        d = n1 % 10
        n1 = n1 // 10
        c = n1 % 10
        m = 1
        n1 = 0
    elif 10 <= n1 <= 99:
        u = n1 % 10
        n1 = n1 // 10
        d = n1 % 10
        c = 1
        m = 1
        n1 = 0
    elif 1 <= n1 <= 9:
        u = n1 % 10
        d = 1
        c = 1
        m = 1
        n1 = 0
    u = u % 2 == 0
    d = d % 2 == 0
    c = c % 2 == 0 
    m = m % 2 == 0
    return u, d, c, m

def main():

    n1 = int(input().strip())
    u, d, c, m = udc(n1)

    if u and d and c and m:
        a = 4
    elif (u and d and c) or (u and d and m) or (u and d and m) or (u and c and m) or (d and c and m):
        a = 3
        print(f'{a}')
    elif (u and d) or (u and c) or (u and m) or (d and c) or (d and m) or (c and m):
        a = 2
        print(f'{a}')
    elif u or d or c or m:
        a = 1
        print(f'{a}')
    else:
        a = 0
        print(f'{a}')

if __name__ == '__main__':
     main()
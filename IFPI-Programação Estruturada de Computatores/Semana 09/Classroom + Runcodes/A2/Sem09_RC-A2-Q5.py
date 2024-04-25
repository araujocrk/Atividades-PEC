def assassino_inocente(a, b, c, d, e):
    if a[0] == 'S' and b[0] == 'S' and c[0] == 'S' and d[0] == 'S' and e[0] == 'S':
        return 'Assassino'
    elif a[0] != 'S' and b[0] != 'S' and c[0] != 'S' and d[0] != 'S' and e[0] != 'S': 
        return 'Inocente'
    elif a[0] == 'S' and b[0] != 'S' and c[0] != 'S' and d[0] != 'S' and e[0] != 'S': 
        return 'Inocente'
    elif b[0] == 'S' and a[0] != 'S' and c[0] != 'S' and d[0] != 'S' and e[0] != 'S': 
        return 'Inocente'
    elif c[0] == 'S' and a[0] != 'S' and b[0] != 'S' and d[0] != 'S' and e[0] != 'S': 
        return 'Inocente'
    elif d[0] == 'S' and a[0] != 'S' and b[0] != 'S' and c[0] != 'S' and e[0] != 'S': 
        return 'Inocente'
    elif e[0] == 'S' and a[0] != 'S' and b[0] != 'S' and c[0] != 'S' and d[0] != 'S': 
        return 'Inocente'
    else:
        return 'Nenhum'
    
def outros(a, b, c, d, e):
    a_i = assassino_inocente(a, b, c, d, e)
    if a_i == 'Assassino':
        return 'Assassino'
    elif a_i == 'Inocente':
        return 'Inocente'
    else:
        if a[0] == 'S' and b[0] == 'S' and a[0] != c[0] and a[0] != d[0] and a[0] != e[0]:
            return 'Suspeito'     
        elif a[0] == 'S' and c[0] == 'S' and a[0] != b[0] and a[0] != d[0] and a[0] != e[0]:
            return 'Suspeito'     
        elif a[0] == 'S' and d[0] == 'S' and a[0] != b[0] and a[0] != c[0] and a[0] != e[0]:
            return 'Suspeito'    
        elif a[0] == 'S' and e[0] == 'S' and a[0] != b[0] and a[0] != c[0] and a[0] != d[0]:
            return 'Suspeito'    
        elif b[0] == 'S' and c[0] == 'S' and b[0] != a[0] and b[0] != d[0] and b[0] != e[0]:
            return 'Suspeito'    
        elif b[0] == 'S' and d[0] == 'S' and b[0] != a[0] and b[0] != c[0] and b[0] != e[0]:
            return 'Suspeito'        
        elif b[0] == 'S' and e[0] == 'S' and b[0] != a[0] and b[0] != c[0] and b[0] != d[0]:
            return 'Suspeito'        
        elif c[0] == 'S' and d[0] == 'S' and c[0] != a[0] and c[0] != b[0] and c[0] != e[0]:
            return 'Suspeito'    
        elif c[0] == 'S' and e[0] == 'S' and c[0] != a[0] and c[0] != b[0] and c[0] != d[0]:
            return 'Suspeito'        
        elif d[0] == 'S' and e[0] == 'S' and d[0] != a[0] and d[0] != b[0] and d[0] != c[0]:
            return 'Suspeito' 
        else:
            return 'Cúmplice'

def main():
    
    #Entrada
    p1 = input().upper().strip()
    p2 = input().upper().strip()
    p3 = input().upper().strip()
    p4 = input().upper().strip()
    p5 = input().upper().strip()
    
    #Processamento
    resultado = outros(p1, p2, p3, p4, p5)
    
    #Saída
    print(f'{resultado}')

if __name__ == '__main__':
    main()
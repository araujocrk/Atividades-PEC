def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
    cidades = carrega_cidades()
    meses = (
        "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
        )
    
    dia = int(input('Insira o dia: '))
    mes = int(input('Insira o mês: '))
    
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {meses[mes - 1]}:')
    
    for uf, _, nome, d, m, _ in cidades:
        if d == dia and m == mes:
            print(f'{nome}({uf})')
if __name__ == "__main__":
    main()
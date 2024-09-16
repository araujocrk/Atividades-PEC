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
    meses = ("JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO")
    
    mes = int(input('Insira o mês: '))
    populacao = int(input('Insira o número de habitantes: '))
    
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {meses[mes - 1]}:')
    
    for uf, _, nome, d, m, pop in cidades:
        if populacao < pop and m == mes:
            print(f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {d} de {meses[mes - 1].lower()}.')

if __name__ == "__main__":
    main()
    
    
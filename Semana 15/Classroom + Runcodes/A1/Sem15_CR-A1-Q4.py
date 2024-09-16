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
    populacao = int(input('Insira o número de habitantes: '))
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for uf, ibge, nome, _, _, pop in cidades:
        if populacao < pop:
            print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}')
if __name__ == "__main__":
    main()

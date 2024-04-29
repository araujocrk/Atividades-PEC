# Define a função remover_acentos recebendo um parâmetro
def remover_acentos(texto):
# Importa do módulo unicodedata a função normalize
    from unicodedata import normalize
# Retorno da função: normaliza o texto em formato NFKD, codifica a string em ASCII ignorando quaisquer caracteres que não possam ser representados em ASCII (Remove os acentos) e decodifica a string de volta para Unicode
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
# Define a função separar_data recebendo um parâmetro
def separar_data(dma):
# A variável 'a' recebe o resto da divisão da variável dma por 10.000
    a = dma % 10000
# A variável 'dma' recebe o resultado da divisão inteira dela mesma por 10.000
    dma //= 10000
# A variável 'm' recebe o resto da divisão da variável dma por 100
    m = dma % 100
# A variável 'dma' recebe o resultado da divisão inteira dela mesma por 100
    dma //= 100
# A variável 'd' recebe a variável 'dma'
    d = dma
# Retorna as variáveis 'd', 'm' e 'a'
    return d, m, a
# Define a função signo recebendo dois parâmetros
def signo(dia, mes):
# Se a variável mes for igual a 3, retorna a string 'Peixes' se a variável dis for menor que 21, senão a string 'Áries'
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
# Se a variável mes for igual a 4, retorna a string 'Áries' se a variável dis for menor que 20, senão a string 'Touro'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
# Se a variável mes for igual a 5, retorna a string 'Touro' se a variável dis for menor que 21, senão a string 'Gêmeos'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
# Se a variável mes for igual a 6, retorna a string 'Gêmeos' se a variável dis for menor que 22, senão a string 'Câncer'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
# Se a variável mes for igual a 7, retorna a string 'Câncer' se a variável dis for menor que 23, senão a string 'Leão'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
# Se a variável mes for igual a 8, retorna a string 'Leão' se a variável dis for menor que 23, senão a string 'Virgem'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
# Se a variável mes for igual a 9, retorna a string 'Virgem' se a variável dis for menor que 23, senão a string 'Libra'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
# Se a variável mes for igual a 10, retorna a string 'Libra' se a variável dis for menor que 23, senão a string 'Escorpião'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
# Se a variável mes for igual a 11, retorna a string 'Escorpião' se a variável dis for menor que 22, senão a string 'Sagitário'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
# Se a variável mes for igual a 12, retorna a string 'Sagitário' se a variável dis for menor que 22, senão a string 'Capricórnio'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
# Se a variável mes for igual a 1, retorna a string 'Capricórnio' se a variável dis for menor que 20, senão a string 'Aquário'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
# Se a variável mes for igual a 2, retorna a string 'Aquário' se a variável dis for menor que 19, senão a string 'Peixes'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'
# Define a função horoscopo recebendo um parâmetro
def horoscopo(signo_desejado):
# Importa o módulo urllib.request (Permite abertura de URLs)
    import urllib.request
# A variável 'signo_formatado' recebe o retorno da função remover_acentos(signo_desejado) e transforma os caracteres em minúsculos
    signo_formatado = remover_acentos(signo_desejado).lower()
# A variável 'minha_url' recebe uma string (url) mais a variável signo_formatado
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo' + '/' + signo_formatado
# A variável 'requisicao' recebe a criação de um objeto 'Request' para solicitar a URL criada anteriormente, definindo também um cabeçalho para simular um navegador web com o User-Agent definido como "Mozilla/5.0".
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
# Abre a URL usando o objeto de solicitação criado e armazena na variável 'resposta'    
    resposta = urllib.request.urlopen(requisicao)
# Lê o conteúdo da página da web como uma sequência de bytes, decodifica-a usando UTF-8 e armazena na variável 'pagina'
    pagina = resposta.read().decode('utf-8')
# Define marcadores para encontrar o início e o final do trecho de texto 
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'
# Encontra a posição do marcador de início na página e define o início do trecho de texto adicionando o comprimento do marcador de início    
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
# Encontra a posição do marcador final a partir da posição de início, definindo assim o final do trecho de texto
    final = pagina.find(marcador_final, inicio)
# Retorna a variável 'signo_desejado' mais a string ': ' e o trecho de texto do horóscopo encontrado entre os marcadores de início e final na página
    return signo_desejado + ': ' + pagina[inicio:final]

def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formado DDMMAAAA: "))
    
    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)
    
    # Saída de dados
    print(horoscopo_de_hoje)
    
# Resumo: O código recebe a data de nascimento do usuário, define seu signo, remove os acentos do signo, procura o horóscopo no site horoscopovirtual e imprime na tela o texto retirado do site

if __name__ == '__main__':
    main()    
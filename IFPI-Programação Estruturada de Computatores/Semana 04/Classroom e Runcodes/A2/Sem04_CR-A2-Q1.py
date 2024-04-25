#As variáveis recebem os valores digitados pelo usuário
v1 = input('Digite um número: ')
v2 = input('Digite outro número: ')
#As variáveis recebem a transformação dos valores acima para float,str e int
v1_float = float(v1)
v2_float = float(v2)
v1_str = str(v1_float)
v2_str = str(v2)
v2_int = int(v2)
#As variáveis recebem os resultados das expressões abaixo
soma = v1_float + v2_int
soma_str = v1_str + v2_str
multi_num = v1_float * v2_float
multi_str = v1_str * v2_int
div_num = v1_float / v2_int
div_num_int = v1_float // v2_int
exponenciacao = v1_float ** v2_int
modulo = v1_float % v2_int
#Imprime na tela os resultados das expressões acima
print(f'a. A soma dos números; {soma}')
print(f'b. A concatenação das strings; {soma_str}')
print(f'c. A multiplicação dos números; {multi_num}')
print(f'd. A multiplicação como strings; {multi_str}')
print(f'e. A divisão dos números; {div_num}')
print(f'f. A divisão inteira dos números; {div_num_int}')
print(f'g. A exponenciação; {exponenciacao}')
print(f'h. O módulo (resto); {modulo}')



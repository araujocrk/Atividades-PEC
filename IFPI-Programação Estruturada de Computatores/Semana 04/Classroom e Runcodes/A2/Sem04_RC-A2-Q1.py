v1 = input().strip()
v2 = input().strip()
v1_float = float(v1)
v2_float = float(v2)
v1_str = str(v1_float)
v2_str = str(v2)
v2_int = int(v2)
soma = v1_float + v2_int
soma_str = v1_str + v2_str
multi_num = v1_float * v2_float
multi_str = v1_str * v2_int
div_num = v1_float / v2_int
div_num_int = v1_float // v2_int
exponenciacao = v1_float ** v2_int
modulo = v1_float % v2_int
print(f'{soma}')
print(f'{soma_str}')
print(f'{multi_num}')
print(f'{multi_str}')
print(f'{div_num}')
print(f'{div_num_int}')
print(f'{exponenciacao}')
print(f'{modulo}')



hora = int(input().strip())
minuto = int(input().strip())
segundo = int(input().strip())
hora_segundo = hora * 3600
minuto_segundo = minuto * 60
seg_passados = hora_segundo + minuto_segundo + segundo
print(f'{seg_passados}')

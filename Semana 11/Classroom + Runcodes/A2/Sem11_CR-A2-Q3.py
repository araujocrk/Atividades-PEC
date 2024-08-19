def main():
    while True: 
        opcao = int(input('OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n').strip())
        if opcao == 0: break
        if opcao > 3 or opcao < 0:
            print(f'Opção inválida.')
        elif opcao == 1:
            print(f'1 - Olá. Como vai?')
        elif opcao == 2:
            print(f'2 - Vamos estudar mais.')
        elif opcao == 3:
            print(f'3 - Meus Parabéns!')
            
    print(f'0 - Fim de serviço.')
        
if __name__ == '__main__':
    main()
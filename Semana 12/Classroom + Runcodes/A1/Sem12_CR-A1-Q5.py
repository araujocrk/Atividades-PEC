

def main():
   
   ano = 1600
   morreram = 0
   nasceram = 0
   pop_aves = int(input('Digite qual era a população de aves no início de 1600: '))
   
   while pop_aves > pop_aves * 0.1:
       morreram = round(pop_aves * 0.06)
       print(f'Morreram {morreram} aves')
       pop_aves -= morreram 
       nasceram = round(pop_aves * 0.01)
       print(f'Nasceram {nasceram} aves')
       pop_aves += (nasceram)
       print(f'Total da população de aves foi {pop_aves}')
       ano += 1
       
if __name__ == "__main__":
    main()
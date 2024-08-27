def main():
   
   ano = 1600
   pop_aves = int(input('Digite qual era a população de aves no início de 1600: '))
   pop_10 = pop_aves * 0.1
   
   while pop_aves > pop_10:
       nasceram = pop_aves * 0.01
       morreram = pop_aves * 0.06
       pop_aves = pop_aves - morreram + nasceram
       print(f'No ano de {ano}: Nasceram {nasceram:.0f}, morreram{morreram:.0f} e ao final sobrou {pop_aves:.0f} pássaros.')
       ano += 1
       
if __name__ == "__main__":
    main()
def main():
   
   ano = 1600
   pop_aves = int(input().strip())
   pop_10 = pop_aves * 0.1
   
   while pop_aves > pop_10:
       nasceram = pop_aves * 0.01
       morreram = pop_aves * 0.06
       pop_aves = pop_aves - morreram + nasceram
       print(f'{ano},{nasceram:.0f},{morreram:.0f},{pop_aves:.0f}')
       ano += 1

if __name__ == "__main__":
    main()
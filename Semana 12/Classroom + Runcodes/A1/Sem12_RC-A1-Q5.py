def main():
   
   ano = 1600
   pop_aves = int(input().strip())
   pop_10 = pop_aves * 0.1
   
   while pop_aves > pop_10:
       morreram = round(pop_aves * (6 / 100))
       nasceram = round(pop_aves * (1 / 100))
       pop_aves = pop_aves - morreram + nasceram
       print(f'{ano},{nasceram},{morreram},{pop_aves}')
       ano += 1

if __name__ == "__main__":
    main()
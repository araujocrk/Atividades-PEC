print("Em que ano você nasceu?")
nascimento = input().strip()
nascimento =int(nascimento)
print("Para qual ano você quer saber sua idade?")
anorandom = input()
anorandom = int(anorandom)
idadeEmrandom = anorandom - nascimento
print("No ano" ,anorandom, "você terá",idadeEmrandom, "anos!")



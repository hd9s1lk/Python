peso = input("Quanto pesas?\n")
print(peso)

unidade= input("(K)g ou (L)bs:\n")
print(unidade)

if unidade == "K" or unidade == "k":
    print(float(peso) / 0.45 )
elif unidade == "L" or unidade == "l":
    print(float(peso) * 0.45)
else:
    print("Não percebo nada disso oh chefe ://")


    
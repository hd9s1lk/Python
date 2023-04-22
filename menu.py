menu="Fino, Shot, Leite"

print("Boas rei, hoje o que vai ser?\n" + menu)

order=input()

price=5

if order == "Fino":
    price = 5
elif order == "Shot":
    price = 2
elif order == "Leite":
    price == 0
else:
    print("Não temos essa merda por aqui.")
    price=0

print(price)


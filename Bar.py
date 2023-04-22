print("Boas tardes, bem vindo ao Raiz Kuadrada!")


name = input("Como te chamas? \n")

if name == "Ben":
    print("Vai po caralho!")
    exit()
else:
    print("Boas " + name + ", como estamos?")


print("Hello " + name + ",thank you so much for coming in today!")

menu = "Black coffe, Espresso, Fino"

print(name + ", what would you like to have today? Where's what we have today:\n" + menu)

order=input()

preco = 8

quant = input("How many would you like?\n")

total= int(quant) * preco

print(total)

print("Thank you! Your total is: " + str(total) + "$")

print("Sounds good! " + name + ", Your " + quant + " " + order + " is coming right away!")





print("Hello, welcome to Raiz Kuadrada")

name = input("What's your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil = input("Are you evil? (Yes/No) \n")
    good = int(input("Quantas boas ações fizeste hoje rei?\n"))
    if evil == "Yes" and good < 4:
        print(name + ", your not welcome here.")
        exit()
    else:
        print("Hello " + name + ", what can i do for you?")
else:
    print("Hello " + name + ", what can i do for you?")

  
nome = input("Qual é o seu nome?\n")
titulo = input("Qual o título da sua história?\n")
personagem = input("Qual o nome do seu personagem?\n")
items=["ak", "granada", "resma de papel", "faca da manteiga", "chocolate"]
inv =[]

print("Esta é a história do/a " + nome + " que tem como título " + titulo + " que nos fala sobre a personagem " + personagem)

direcao =input("O seu personagem pode escolher 4 direções diferentes para prosseguir: Norte, Sul, Este ou Oeste. Qual deseja seguir?\n")

if direcao == "Norte":
    print("O seu personagem seguiu para norte. Encontrou o mítico hacker lécio que destruiu todas as suas células cerebrais. GAME OVER")
    exit()
elif direcao =="Sul":
    print("O seu personagem seguiu para sul. Encontrou heim god lvl 11 reddit. Recebeu um(a) " + items[0] + "!" + " O seu personagem prosseguiu e encontrou a aldeia: LOUSADA!")
elif direcao =="Este":
    print("""O seu personagem seguiu para Este. Morreste.. BAZINGA PUNK. Encontras-te uma aldeia, LOUSADA, onde ao portão te deram um """ + items[4] + "!")
elif direcao == "Oeste":
    print("O seu personagem seguiu para Oeste. Encontrou a aldeia: LOUSADA ")
else:
    print("Não escolheu nenhuma direção. O seu personagem morreu à fome... GAME OVER")
    exit()

print("O seu personagem andou um pouco pela aldeia e encontrou uma mochila velha. Terá a opção de abrir o seu inventário!")


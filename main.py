import random

print("===================================")
print("BEM VINDO À CRÔNICAS DA NÉVOA")
print("===================================")
print("Bem vindo ou mundo...")
nome = input("Digite o nome do seu Personagem: ")
print(f"Bem Vindo {nome}!")

personagem = {
    "nome" : nome,
    "vida" : 100,
    "mana" : 50,
    "ataque" : 10,
    "defesa" : 5,
    "ouro" : 10,
    "xp" : 0
}



class Inimigo:
    def __init__(self,nome,vida,ataque,defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebe {dano} de dano.")



def mostrar_status(personagem):
    vida = personagem["vida"]
    mana = personagem["mana"]
    ataque = personagem["ataque"]
    defesa = personagem["defesa"]
    ouro = personagem["ouro"]
    xp = personagem["xp"]
    status = f"---STATUS---\nVida: {vida}\nMana: {mana}\nAtaque: {ataque}\nDefesa: {defesa}\nOuro: {ouro} \nXP: {xp}"
    return status

ENCONTROS = {
    "Goblin": Inimigo("Goblin",30,5,3),
    "Lobo": Inimigo("Lobo",36,6,3)
}



while True:
    opcao = input("O que você deseja fazer? \n1 - Explorar \n2 - Ver status \n3 - Sair\n")

    if opcao == "1":
        print("Você decidiu explorar...")
        print("Você entra em uma floresta coberta pela névoa.")
        opcao = input("Você encontra dois caminhos: \n1 - Seguir pela trilha \n2 - Voltar \nEscolha:")
        if opcao == "1":
            encontros_exploracao = ["Goblin", "Lobo","Baú"]
            escolha_aleatoria = random.choice(encontros_exploracao)
            inimigo_encontrado = None
            if escolha_aleatoria in ENCONTROS:
                inimigo_encontrado = ENCONTROS[escolha_aleatoria]
                
            print("Voce decidiu Seguir pela trilha...")

            if inimigo_encontrado != None:
                print(f"Voce acaba de encontrar {inimigo_encontrado.nome}, ele possui {inimigo_encontrado.vida} de vida.")
                opcao = input("O que deseja fazer?\n1. Atacar \n 2. Fugir\n")
                if opcao == "1":
                    inimigo_encontrado.receber_dano(personagem["ataque"])
                elif opcao == "2":
                    pass
                else:
                    print("Opção inválida!")
            else:
                print(f"Voce encontrou {escolha_aleatoria}")
        elif opcao == "2":
            print("Vece decidiu voltar")
        else:
            print("Opção inválida!")
    elif opcao == "2":
        status = mostrar_status(personagem)
        print(status)
    elif opcao == "3":
        print("Voce saiu do Jogo!")
        break
    else:
        print("Opção invalida!")

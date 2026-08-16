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

print(personagem)


def mostrar_status(personagem):
    vida = personagem["vida"]
    mana = personagem["mana"]
    ataque = personagem["ataque"]
    defesa = personagem["defesa"]
    ouro = personagem["ouro"]
    xp = personagem["xp"]
    status = f"---STATUS---\nVida: {vida}\nMana: {mana}\nAtaque: {ataque}\nDefesa: {defesa}\nOuro: {ouro} \nXP: {xp}"
    return status

while True:
    opcao = input("O que você deseja fazer? \n1 - Explorar \n2 - Ver status \n3 - Sair\n")

    if opcao == "1":
        print("Você decidiu explorar...")
        print("Você entra em uma floresta coberta pela névoa.")
        opcao = input("Você encontra dois caminhos: \n1 - Seguir pela trilha \n2 - Voltar \nEscolha:")
        if opcao == "1":
            encontros_exploracao = ["Goblin", "Lobo","Baú"]
            escolha_aleatoria = random.choice(encontros_exploracao)
            print("Voce decidiu Seguir pela trilha...")
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

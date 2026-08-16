
print("===================================")
print("BEM VINDO À CRÔNICAS DA NÉVOA")
print("===================================")
print("Bem vindo ou mundo...")
nome = input("Digite o nome do seu Personagem: ")
print(f"Bem Vindo {nome}!")

vida = 100
mana = 50
ataque = 10
defesa = 5
ouro = 10
xp = 0

print(f"---STATUS---\nVida: {vida}\nMana: {mana}\nAtaque: {ataque}\nDefesa: {defesa}\nOuro: {ouro} \nXP: {xp}")

opcao = input("O que você deseja fazer? \n1 - Explorar \n2 - Ver status \n3 - Sair")

if opcao == "1":
    print("Você decidiu explorar!")
elif opcao == "2":
    print(f"---STATUS---\nVida: {vida}\nMana: {mana}\nAtaque: {ataque}\nDefesa: {defesa}\nOuro: {ouro} \nXP: {xp}")
elif opcao == "3":
    print("Voce saiu do Jogo!")
else:
    print("Opção invalida!")

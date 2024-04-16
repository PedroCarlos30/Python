nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18 and idade <= 59:
    print(f"{nome}, você tem {idade} por tanto você é maior de idade.")
if idade >= 60:
    print(f"{nome} você tem {idade} por tanto você é idoso.")
if idade < 18:
    print(f"{nome}, você tem {idade} por tanto você não é maior de idade.")


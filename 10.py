while True:
    idade = input("Qual a idade da pessoa? ")
    if idade == "sair":
        break
    idade = int(idade)
    if idade < 3:
        preco = 0
    elif idade <= 12:
        preco = 15
    else:
        preco = 30
    print(f"O preço do ingresso é R$ {preco:.2f}")

print("Programa encerrado.")
preco = float(input("Qual é o preço do produto? R$"))
novo = preco - (preco * 5 / 100)

print(f"O produto custava R${preco} e agora com o desconta de 5%, o produta está custando R${novo:.2f}")
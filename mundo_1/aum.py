sal = float(input("Qual é o salário? R$"))
novo = sal + (sal * 15 / 100)

print(f"O funcionário ganhava R${sal} e agora com o aumento de 15%, o fucionário ganha R${novo:.2f}")
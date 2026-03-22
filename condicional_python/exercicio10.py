import os 
os.system("cls")


prod1 = float(input("Qual é o valor do produto: "))


print(f"Valor do Produto é ${prod1}")
if prod1 > 100:
    print("Você ganhou 10% de desconto!")
else:
    print("Você ganhou 5% de desconto!")
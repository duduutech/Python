import os 
os.system("cls")

compra_user = int(input("Qual é o valor do produto: "))
valor_des = (compra_user * 7.5) / 100

print(f"Compra: {compra_user}")

if compra_user > 5000:
    print(f"Valor Original R$ {compra_user}")
    print (f"Com desconto R$ {valor_des}")


import os 
os.system("cls")

sal1 = int(input("Salário-Fixo: "))
venda_mes = int(input("Venda do Mês: "))



if venda_mes > 100000:
    bonus1 = sal1 * 2
    print(f"Bônus de R$ {bonus1}")
elif venda_mes == 100000:
    bonus2 = sal1 * 1.5
    print(f"Bônus de R$ {bonus2}")
else:
    print("Sem bonus!")

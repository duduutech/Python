import os 
os.system("cls")

numero = int(input("Digite qual tabuada você quer: "))

for i in range (1, 11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
            
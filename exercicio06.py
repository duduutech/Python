import os 
os.system("cls")

num1 = int(input("Escola um número: "))
num2 = int(input("Escolha outro número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
else:
    print(f"O maior número é {num2}")
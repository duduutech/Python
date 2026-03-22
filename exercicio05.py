import os 
os.system("cls")


num1 = int(input("Digite um número para saber se é multiplo de 5: "))
num2 = num1 + (5 - num1 % 5)

if num1 % 5 == 0 : 
    print(f"O número {num1} é multiplo de 5")
if num1 + (5 - num1 % 5):
    print(f"O número {num1} não é multiplo de 5, porém o próximo numero multiplo de 5, será: {num2}")

import os
os.system("cls")

#Pedir ao usuário o valor dos 4 números
num1 = int(input("Digite o valor de X1: "))
num2 = int(input("Digite o valor de X2: "))
num3 = int(input("Digite o valor de X3: "))
num4 = int(input("Digite o valor de X4: "))

# Calculo Referencial
media = (num1 + num2 + num3 + num4)/4

#Imprimir texto 
print(f"A média entre os valores de X é {media}")
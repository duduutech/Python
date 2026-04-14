import os
os.system("cls")

soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero

    media = soma / 5 
   
print(f"A média é igual a: {media}")
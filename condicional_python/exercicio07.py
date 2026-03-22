import os 
os.system("cls")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 5:
    print (f"Média {media:0} - Aprovado")
else:
    print(f"Média {media:0} - Reprovado")
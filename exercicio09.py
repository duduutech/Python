import os 
os.system("cls")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2


if nota1 < 0:
    print(f"Nota {nota1} Invalida!")
elif nota1 > 10:
    print(f"Nota {nota1} Invalida!")

elif nota2 > 10:
    print(f"Nota {nota2} Invalida!")
elif nota2 < 0:
    print(f"Nota {nota2} Invalida!")


if media >= 5:
    print (f"Média {media:0} - Aprovado")
elif media < 5:
    print(f"Média {media:0} - Reprovado")
else:
    print(f"Nota Invalida {nota1}")
    print(f"Nota Invalida {nota2}")
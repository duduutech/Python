import os 
os.system("cls")

nota = float(input("Qual é a nota: "))

if nota <= 10: 
    print(f"{nota} é uma nota válida.")
elif nota < 0:
    print(f"{nota} é uma nota inválida.")
elif nota > 10:
    print(f"{nota} é uma nota inválida")

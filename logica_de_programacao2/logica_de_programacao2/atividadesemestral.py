import os 
os.system("cls")

sal_minimo = 1302.00

sal = float(input("Salário: R$ "))

if sal < 0:
    print("ERRO! Digite um salário positivo.")
else:
    faltas = int(input("Qtd. De Faltas: "))

    if faltas < 0:
        faltas = 0

    if sal_minimo * 10 <= sal and sal <= sal_minimo * 15:
        reajuste = sal * 0.012
    else:
        reajuste = 0

    salario_reajustado = sal + reajuste

  
    if faltas == 0:
        bonus = sal_minimo * 2
    elif faltas <= 2:
        bonus = sal_minimo
    elif faltas <= 5:
        bonus = sal_minimo * 0.5
    else:
        bonus = 0

    ganho_total = salario_reajustado + bonus

    print("\nRelatório:")
    print(f"Salário.............: R$ {sal:.2f}")
    print(f"Salário Reajustado..: R$ {salario_reajustado:.2f}")
    print(f"Bônus...............: R$ {bonus:.2f}")
    print(f"Ganho total.........: R$ {ganho_total:.2f}")
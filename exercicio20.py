import os 
os.system("cls")

s_ass = float(input("Salário: R$ "))


if s_ass <= 2259.20:
    print("Sem Imposto de Renda")
elif s_ass >= 2259.21 and s_ass <= 2829.65:
    v1 = (s_ass * 0.075) - 169.44
    print(f"IR R$ {v1}")
elif s_ass >= 2826.66 and s_ass <= 3751.05:
    v2 = (s_ass * 0.15) - 381.44
    print(f"IR R$ {v2}")
elif s_ass >= 3751.06 and s_ass <= 4664.68:
    v3 = (s_ass * 0.225) - 662.77
    print(f"IR R$ {v3:.2f}")
elif  s_ass > 4664.68:
    v4 = (s_ass * 0.275) - 896
    print(f"IR R$ {v4:.2f}")
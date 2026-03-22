import os 
os.system("cls")

s_ass = float(input("Salário: R$ "))

if s_ass >= 0 and s_ass <= 1.518:
    valor1 = (s_ass * 7.50) / 100
    print(f"INSS R$ {valor1} ")

elif s_ass > 1518 and s_ass <= 2793.88:
    valor2 = s_ass * 9/ 100
    print(f"INSS R$ {valor2}")

elif s_ass > 2793.88 and s_ass <= 4190.83:
    valor3 = s_ass * 0.12
    print(f"INSS R$ {valor3} ")
    
elif s_ass >= 4190.83 and s_ass < 8157.41:
    valor4 = s_ass * 0.14
    print(f"INSS R$ {valor4}")
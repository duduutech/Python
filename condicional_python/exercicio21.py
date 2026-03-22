import os 
os.system("cls")

s_ass = float(input("Salário: R$ "))


#INSS
if s_ass >= 0 and s_ass <= 1.518:
    inss = (s_ass * 7.50) / 100
   

elif s_ass > 1518 and s_ass <= 2793.88:
    inss = s_ass * 9/ 100
   

elif s_ass > 2793.88 and s_ass <= 4190.83:
    inss = s_ass * 0.12
    
    
elif s_ass >= 4190.83 and s_ass < 8157.41:
    inss = s_ass * 0.14
    




#IR 
if s_ass <= 2259.20: 
    ir = 0
    
elif s_ass >= 2259.21 and s_ass <= 2829.65:
    ir = (s_ass * 0.075) - 169.44
    
elif s_ass >= 2826.66 and s_ass <= 3751.05:
    ir = (s_ass * 0.15) - 381.44
    
elif s_ass >= 3751.06 and s_ass <= 4664.68:
    ir = (s_ass * 0.225) - 662.77
    
elif  s_ass > 4664.68:
    ir = (s_ass * 0.275) - 896
    

liquido = s_ass - inss - ir

print(f"Salário .........: R$ {s_ass}")
print(f"INSS.........: R$ {inss}")
print(f"IR.........: R$ {ir}")
print(f"Salário Liquido.........: R$ {liquido}")

import os 
os.system("cls")


n1 = float(input("Numero 01: "))
n2 = float(input("Numero 02: "))
n3 = float(input("Numero 03: "))

if n1 > n2 and n1 < n3:
    print(f"O valor Intermediário é {n1}")
elif n2 > n1 and n2 < n3:
    print(f"O valor Intermediario é {n2}")
else:
    print(f"O valor Intermediario é {n3}")
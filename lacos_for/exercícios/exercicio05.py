import os 
os.system("cls")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))


if n1 < n2:
    for i in range(n1, n2 + 1, 1):
        print(i)
else:
    for i in range(n1, n2 - 1, -1):
        print(i)
import os
os.system("cls")

valorX = float(input("Digite um número para saber seu módulo: "))
 
if valorX < 0:
    modulo = valorX * -1
    print("O módulo do valor ", valorX, " é ", modulo )

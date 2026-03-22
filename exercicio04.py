import os 
os.system("cls")


print("============================================================================")
numberX = int(input("Escolha um número para saber se ele é par ou ímpar: ")) 
print("============================================================================")

if numberX % 2 == 0:
    print("Numero é par")
else:
    print("Numero é impar")
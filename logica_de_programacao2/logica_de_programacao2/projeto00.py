import os 
os.system("cls")

nome1 = "Marcelo Marques Ferreira" 
nome2 = "Maria Silva"
valor1 = 8450
valor2 = 45 
valor3 = 45.9687
valor4 = 3455.456



#Finalizando Formatações
print(f"Nome......: | {nome1:40s}{nome2:40s}|")

print(f"Nome......: | {nome1}|{nome2}|")

print(f"Name....: {valor1}")


print(f"Valor 1...: |{valor1: 7d}|")
print(f"Valor 1...: |{valor1: 07d}|")
print(f"Valor 2...: |{valor1: 7d}|")
print(f"Valor 2...: |{valor1: 07d}|")

print(f"Valor 3...: |R${valor3: 10.2f}|")
print(f"Valor 4...: |R${valor4: 10.2f}|")


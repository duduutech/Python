import os 
os.system("cls")

# 1. Entrada de dados
valor = int(input("Digite o valor que deseja sacar: "))

# 2. Processamento das notas de 100
n100 = valor // 100
valor = valor % 100

# 3. Processamento das notas de 50
n50 = valor // 50
valor = valor % 50

# 4. Processamento das notas de 20
n20 = valor // 20
valor = valor % 20

# 5. Processamento das notas de 10
n10 = valor // 10
valor = valor % 10

# 6. Exibição dos resultados

print(f"""Notas de R$ 100: {n100}
      Notas de R$ 50: {n50}
      Notas de R$ 20: {n20}
      Notas de R$ 10: {n10}""")

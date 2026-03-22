import os 
os.system ("cls")

#Entrada de dados 
num = int(input("Digite um número: ") )

#Entrada de Dados
exit_n = num % 5
falta = 5 - exit_n
soma = falta + num
nxm = soma

#Saída de dados
print(f"O próximo número múltiplo de 5 é {soma}")
print(f"A divisão entre {num} e 5 tem como resto divisional {exit_n}")
print(f"Com isso o próximo número múltiplo de 5 é {nxm}")

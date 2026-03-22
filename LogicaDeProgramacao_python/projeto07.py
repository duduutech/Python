import os 
os. system("cls")




#Entrada de dados 
num_client = int(input("Qual o valor desejado: "))
boxe_num = num_client

c1 = num_client // 50
num_client = num_client % 50
c2 = num_client // 20
num_client = num_client % 20
c3 = num_client // 10
num_client = num_client % 10


#Saída de dados 
print(f"Valor desejado: {boxe_num}")
print(f"Relatório de cédulas para compor a quantia desejada : {c1}, {c2}, {c3}")




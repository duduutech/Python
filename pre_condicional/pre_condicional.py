
import os 
os.system("cls")



# 1. Forçar o usuário a digitar uma nota válida (entre 0 e 10) e no final mostrar a nota
# com o seu devido casting
#   TESTE
#   Nota: edson
#   ERRO! Digite uma nota válida!
#   Nota: 87
#   ERRO! Digite uma nota válida!
#   Nota: -2
#   ERRO! Digite uma nota válida!
#   Nota: 10
#   Você digitou uma nota válida!



# 2. Dadas duas notas pelo usuário, verificar se ele está "Aprovado" (ao menos 6), 
# reprovado (abaixo de 4) ou em "Exame" (entre 4 e 5.9).
# *** forçar o usuário a digitar notas válidas
#   TESTE
#   Nota 1: ABC
#   ERRO! Digite uma nota válida!
#   Nota 1: 34
#   ERRO! Digite uma nota válida!
#   Nota 1: 8
#   Nota 2: -34
#   ERRO! Digite uma nota válida!
#   Nota 2: 9
#   Aprovado! Media = 9.5



"""
#Calcular o dobro de um numero dado pelo usuário

while True: 
    numero = input("Numero: ")
    if not numero.isnumeric():
        print("ERRO! Não digitou um numero!")
        continue 
    else: 
        break 

numero = float(numero) 


print("Dobro: ", numero + numero)
"""




"""
#Calcular o dobro de um numero dado pelo usuário
numero = input("Numero:")

#Tratamento da não digitação de um numero!
while not numero.isnumeric():  #Enquanto não for um numero faça!
    print("Erro! Não digitou um numero!")
    numero = input("Numero: ")
else:
    numero = float(numero) #Se nao houver interrupção!



numero  = float(numero)
print("Dobro: ", numero + numero)
"""



"""
Exemplo: Força o usuário a digitar um número.

Execução 1:
Numero: 6
Digitou o numero 6 

Execução 2:
Numero: ABC
Erro! Digite m número 
Numero: @
Erro! Digite um número
Digitou o numero 6 

"""


"""
if numero.isnumeric():
    print(f"{numero} é um numero")
else:
    print(f"{numero} não é um numero")
"""



"""
valo = "34"
print(valor.isnumeric()) #retornar true se a string for numerica, senao False
valor ="ABC"
print(valor.isnumeric()) #retornar true se a string for numerica, senao False
"""

"""
Nivel estagiario
numero = int(input("Numero: "))
print(numero, type(numero))
"""
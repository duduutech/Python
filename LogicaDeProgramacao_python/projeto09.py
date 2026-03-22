import os 
os.system("cls")

nome = (input("Qual é o seu nome: "))
idade = int(input("Qual é o sua idade: "))
doença_infeci = input("Suspeita de doença contagiosa? ".upper())

if idade >= 65 and doença_infeci == "SIM":
    print("O paciente será direcionado para sala AMARELA - Com prioridade")
elif idade < 65 and doença_infeci == "SIM":
    print(" O paciente será direcionado para a sala AMARELA - Sem prioridade")
elif idade >= 65 and doença_infeci == "NÃO":
    print(" O paciente será transferido para a sala BRANCA - COM prioridade")
elif idade < 65 and doença_infeci == "NÃO":
    print("O paciente será transferido para a sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença com SIM ou NÃO")
import os 
os.system("cls")


pre_cig = float(input("Qual é o preço do cigarro: "))
qntd_maco = float(input("Quantidade de maços consumidos: "))
temp_anos = int(input("Anos que a pessoa fuma: "))


#calculo 
cal_anos = (pre_cig * qntd_maco * temp_anos * 365)

#Saída 
print(f"Essa pessoa fuma há: {cal_anos}")
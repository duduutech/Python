import os 
os.system ("cls")


#Pedir valores numéricos 
km = float(input("Quilometragem que o veículo percorreu em KM: "))
litros = float(input("Quantidade de litros gasto na quilometragem: "))


#Cáculo 
form_math = km/litros 

#Saída de dados
print(f"A quantidade de quilometros por litro que o carro percorreu foi de {form_math}")

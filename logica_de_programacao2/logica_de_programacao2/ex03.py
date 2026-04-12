import os 
os.system("cls")

temp_fahrenheit = float(input("Quantos graus em Fahrenheit: "))

temp_celsius = (temp_fahrenheit - 32 ) / 1.8

print (f"A conversão de Fahrenheit para Graus Celsius é {temp_celsius:.2f}")
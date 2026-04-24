import os 
os.system("cls")

v = [45, -89, 32, -12, 33]

print(v[0], v[-1])

# -------------------------------------------
v = [45, -89, 32, -12, 33]

for i in range(0, len(v), 2 ):
    print(v[i])

# -------------------------------------------
v = [45, -89, 32, -12, 33]

print( )
numero= int(input("Digite um numero: "))

if numero in v:
    print(f"O numero {numero} na lista é valido")
else:
    print("Invalido")
   


# -------------------------------------------

       


print( )
v = [45, -89, 32, -12, 33]

print(v)
print(v[0])

# -----------------------------------------------

print()
for elem in v:
    if elem < 0:
        print(elem, end = " ")

# -----------------------------------------------

print(sum(v)) #programador nutela

print()
soma = 0 
for elem in v:
    soma += elem
    print (soma)
    
# -----------------------------------------------

def calcular_soma(v:list) -> int:
    soma = 0

    for elem in v:
        soma += elem
    return soma 

# -----------------------------------------------

media = calcular_soma(v) / len(v)
media = soma / len(v)
print(media)

# -----------------------------------------------

v = [45, -89, 32, -12, 33]

for elem in v: 
    if elem % 2 == 1: #"se elemento for impar"
        print(elem, end = " ")
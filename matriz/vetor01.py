import os 
os.system("cls")

#Criando um "vetor"
#     0   1   2    3  4    <-- indices 
#    -5  -4  -3   -2  -1    <-- indices negativos
v = [45, 56, 76, -45, 34]

print(v)
print(v[0])
print(v[4])
print(v[-1])


print(len(v))  #    Retorna a quantiidade de elementos - 5
print(len("eduardo"))  # Retorna 7 caracteristicas


#     0   1   2    3  4    <-- indices 
v = [45, 56, 76, -45, 34]
for ind in range (0, len(v), 1 ):
    print(ind, v[ind]) # traz o numero do indice e o conteudo

for elem in v:
    print(elem, end = " ") #elem - pegar o conteúdo que esta na variavel


print()
for ind, elem in enumerate(v):
    print(f"{ind} - {elem} - ", end = " | ")





soma = [v]

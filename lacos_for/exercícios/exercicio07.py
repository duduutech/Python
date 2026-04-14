import os 
os.system("cls")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
ordem = input("Ordem crescente ou decrescente: ")

if n1 < n2 and ordem == "crescente":
    for i in range(n1, n2 + 1, 1):
        print(i)
elif n1 > n2 and ordem == "decrescente":
    for i in range(n1, n2 - 1, -1):
        print(i)
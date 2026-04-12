import os 
os.system("cls")

valorX = int(input("Digite um valor: "))

resto = valorX % 5

if resto == 0:
    proximo = valorX + 5
else:
    proximo = valorX + (5 - resto)
print(f"Próximo numero multiplo de 5: {proximo}")
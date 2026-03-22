import os 
os.system("cls")

prodt = float(input("Compra: "))
pag = int(input("Forma de Pagamento: "))

if pag == 1:
    desc = (prodt * 0.95)
    print(f"Valor Original:{prodt}")
    print(f"Valor ajustado: {desc}")
elif pag == 2:
    print(f"O valor é {prodt}")
elif pag == 3:
    desc2 = (prodt * 1.1)
    print(f"Valor Original:{prodt}")
    print(f"Valor ajustado: {desc2}")
elif pag == 4:
    desc2 = (prodt * 1.025)
    print(f"Valor Original:{prodt}")
    print(f"Valor ajustado: {desc2}")


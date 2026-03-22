import os 
os.system("cls")

L1 = int(input(" Lado A: "))
L2 = int(input(" Lado B: "))
L3 = int(input(" Lado C: "))

if L1 + L2 > L3: 
    print(f"Os lados {L1, L2, L3} formam um triângulo")
elif L1 + L3 > L2:
    print(f"Os lados {L1, L2, L3} formam um trinângulo")
elif L3 + L2 > L1: 
    print(f"Os lados {L1, L2, L3} formam um triângulo")
else:
    print(f"Os lados {L1, L2, L3} não formam um triângulo")
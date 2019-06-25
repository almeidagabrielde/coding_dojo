print("****************************************")
print("        *** CALCULO NOTAS ***")
print("****************************************")

nota_ac = float(input("Digite sua nota de AC: "))
nota_ai = float(input("Digite sua nota de AI: "))
nota_as = float(input("Digite sua nota de AS: "))

media_final = (nota_ac * 0.25 + nota_ai * 0.30 + nota_as * 0.45)
print("+--------------------+")
print("|                    |")
print("|                    |")
if media_final >= 6:
    print("   ", media_final, "Aprovado")
else:
    print("   ", media_final, "Reprovado")
print("|                    |")
print("+--------------------+")

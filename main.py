bruto = input("Bruto iznos? ")
dalipio = input("Pio? ")
osnovica = float(str(round(int(bruto) * 0.696, 2)))
porez = float(str(round(osnovica * 0.09, 2)))
if(dalipio == "da"):
    pio = float(str(round(osnovica * 0.205, 2)))
else:
    pio = 0
prirez = float(str(round((porez + pio) * 0.1, 2)))
neto = float(str(round(int(bruto) - porez - pio - prirez, 2)))

print(f"Bruto iznos je {bruto} porez je {porez} prirez je {prirez} pio je {pio} neto je {neto}")
print(f"Uplatiti osobi {neto} eura, a porez {porez + pio} eura")

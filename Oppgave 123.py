name = input("Hva heter du? ")
age = input("Hvor gammel er du? ")
print(f"Hei {name}, du er {age} år gammel.")

print("Kalkulator")
en = input("Første siffer ")
to = input("Andre siffer ")
svar = int(en) + int(to)
print(f"Summen av {en} og {to} er {svar}.")

sjekk = input("Er du gammel nok til å ta førekoret? skriv inn alderen din ")
if int(sjekk) >= 18:
    print("Du er gammel nok")
else:
    print("Du er ikke gammel nok")

k = input("Hva fikk du som karakter? (0-100) ")
if int(k) >= 97:
    print("Du fikk karakteren A+")
elif int(k) >= 93:
    print("Du fikk karakteren A")
elif int(k) >= 90:
    print("Du fikk karakteren A-")
elif int(k) >= 87:
    print("Du fikk karakteren B+")
elif int(k) >= 83:
    print("Du fikk karakteren B")
elif int(k) >= 80:
    print("Du fikk karakteren B-")
elif int(k) >= 77:
    print("Du fikk karakteren C+")
elif int(k) >= 73:
    print("Du fikk karakteren C")
elif int(k) >= 70:
    print("Du fikk karakteren C-")
elif int(k) >= 67:
    print("Du fikk karakteren D+")
elif int(k) >= 63:
    print("Du fikk karakteren D")
elif int(k) >= 60:
    print("Du fikk karakteren D-")
elif int(k) < 60:
    print("Du fikk karakteren F")

print("Takk for at du brukte karakter kalkulatoren, tallene er fra MITs karakter skala.")
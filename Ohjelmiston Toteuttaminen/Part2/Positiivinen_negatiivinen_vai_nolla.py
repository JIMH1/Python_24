"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjää syöttämään luvun ja kertoo, onko luku positiivinen, negatiivinen vai nolla. Käytä if,elif, else rakennetta. """

# Pyydetään käyttäjältä lukua
luku = float(input("Syötä luku: "))

# Tarkistetaan luvun arvo if-elif-else rakenteella
if luku > 0:
    print("Luku on positiivinen.")
elif luku < 0:
    print("Luku on negatiivinen.")
else:
    print("Luku on nolla.")
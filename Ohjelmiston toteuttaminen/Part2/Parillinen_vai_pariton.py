"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjää syöttämään kokonaisluvun ja kertoo, onko luku parillinen vai pariton. """

# Pyydetään käyttäjältä kokonaislukua
luku = int(input("Syötä kokonaisluku: "))

# Tarkistetaan, onko luku parillinen vai pariton
if luku % 2 == 0:
    print("Luku on parillinen.")
else:
    print("Luku on pariton.")

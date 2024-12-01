"""  Tehtävänanto

Kirjoita funktio suurin, joka ottaa parametrinä kolme lukua ja palauttaa niistä suurimman.
 """
# Määritellään funktio, joka ottaa kolme parametria
def suurin(luku1, luku2, luku3):
    return max(luku1, luku2, luku3)  # Palautetaan suurin luku

# Kutsutaan funktiota ja tulostetaan suurin luku
tulos = suurin(10, 25, 15)
print(f"Suurin luku on {tulos}.")

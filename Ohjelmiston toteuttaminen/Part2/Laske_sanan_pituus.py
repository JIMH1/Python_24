"""  Tehtävänanto

Kirjoita funktio sanan_pituus, joka ottaa parametrinä sanan ja palauttaa sen pituuden.
 """
# Määritetään funktio sanan_pituus
def sanan_pituus(sana):
    return len(sana)

# Esimerkki käyttö
sana = "esimerkki"
pituus = sanan_pituus(sana)
print(f"Sanan '{sana}' pituus on {pituus} merkkiä.")

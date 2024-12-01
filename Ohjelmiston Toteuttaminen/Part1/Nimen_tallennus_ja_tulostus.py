"""  Tehtävänanto

    Luo muuttuja nimi ja tallenna siihen oma nimesi.
    Tulosta nimi ja tervehdys kolmella eri tavalla:
        Pilkun avulla: Pilkku erottaa muuttujan ja tekstin, ja tulostus tapahtuu automaattisesti välilyönnillä erotettuna.
        f-string-muotoilulla: Käytä Pythonin f-string-ominaisuutta muotoillaksesi tulostettavan tekstin.
        Plusmerkki-konkatenaatiolla: Yhdistä merkkijonoja ja muuttujia käyttäen +-merkkiä.

Tulostuksen tulee olla seuraavassa muodossa:

“Hei <nimesi>! Kiva nähdä sinua!” """


    # Pilkun avulla: Pilkku erottaa muuttujan ja tekstin, ja tulostus tapahtuu automaattisesti välilyönnillä erotettuna.
etunimi = "Juha-Matti"
sukunimi = "Huhtala"

print("Hei", etunimi, sukunimi, "! Kiva nähdä sinua!")

    # f-string-muotoilulla: Käytä Pythonin f-string-ominaisuutta muotoillaksesi tulostettavan tekstin.
nimi ="Juha-Matti Huhtala"
print(f"Hei {nimi}! Kiva nähdä sinua!")

    # Plusmerkki-konkatenaatiolla: Yhdistä merkkijonoja ja muuttujia käyttäen +-merkkiä
nimi = "Juha-Matti Huhtala"
print("Hei " + nimi + "! Kiva nähdä sinua!")
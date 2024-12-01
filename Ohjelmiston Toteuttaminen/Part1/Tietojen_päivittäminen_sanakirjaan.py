"""  Tehtävänanto

    Sanakirjan luominen: Luo sanakirja nimeltä auto, joka sisältää seuraavat avain-arvo-parit:
        merkki: Auton merkki (merkkijonona, esim. "Toyota")
        malli: Auton malli (merkkijonona, esim. "Corolla")
        vuosimalli: Auton vuosimalli (kokonaislukuna, esim. 2018)

    Sanakirjan tulostaminen ennen päivitystä: Tulosta sanakirjan tiedot ennen kuin teet siihen muutoksia. Tämä auttaa sinua näkemään, miten tiedot ovat alun perin tallennettu sanakirjaan.

    Sanakirjan päivittäminen: Päivitä auton vuosimalli sanakirjassa. Valitse uusi vuosimalli (esim. 2022) ja päivitä se sanakirjaan käyttämällä avainta vuosimalli.

    Sanakirjan tulostaminen päivityksen jälkeen: Tulosta päivitetty sanakirja, jotta näet muutokset. Näin voit vertailla alkuperäisiä tietoja ja päivitettyjä tietoja keskenään. """

  # Luodaan sanakirja nimeltä auto
auto = {
    "merkki": "Toyota",
    "malli": "Corolla",
    "vuosimalli": 2018
}

# Tulostetaan sanakirja ennen päivitystä
print("Sanakirja ennen päivitystä:", auto)

# Päivitetään auton vuosimalli
auto["vuosimalli"] = 2022

# Tulostetaan sanakirja päivityksen jälkeen
print("Sanakirja päivityksen jälkeen:", auto)

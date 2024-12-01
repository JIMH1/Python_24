"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjältä pistemäärän (0–100) ja tulostaa sen perusteella arvosanan:

    90–100: Erinomainen
    75–89: Hyvä
    50–74: Tyydyttävä
    Alle 50: Hylätty """

# Pyydetään käyttäjältä pistemäärää
pisteet = int(input("Syötä pistemäärä (0–100): "))

# Tarkistetaan pistemäärän perusteella arvosana
if pisteet >= 90 and pisteet <= 100:
    print("Arvosana: Erinomainen")
elif pisteet >= 75 and pisteet <= 89:
    print("Arvosana: Hyvä")
elif pisteet >= 50 and pisteet <= 74:
    print("Arvosana: Tyydyttävä")
elif pisteet < 50:
    print("Arvosana: Hylätty")

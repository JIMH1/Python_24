"""  Tehtävänanto

Tehtävänäsi on luoda sanakirja, joka tallentaa yhden henkilön perustiedot. Sanakirjan avulla voit tallentaa avain-arvo-pareja, missä avain kuvaa tiedon tyyppiä (esim. nimi) ja arvo sisältää varsinaisen tiedon (esim. henkilön nimi).

Ohjeet:

    Luo sanakirja nimeltä henkilo, joka sisältää seuraavat avain-arvo-parit:
        nimi: Henkilön nimi (merkkijonona, esim. "Laura Virtanen")
        ikä: Henkilön ikä (kokonaislukuna, esim. 28)
        kaupunki: Henkilön asuinkaupunki (merkkijonona, esim. "Helsinki")

    Kun olet luonut sanakirjan, tulosta se kokonaisuudessaan yhdellä komennolla. Tämä auttaa sinua näkemään, miten Python esittää sanakirjojen sisältöä.
 """
  # Luodaan sanakirja nimeltä henkilo
henkilo = {
    "nimi": "Laura Virtanen",
    "ikä": 28,
    "kaupunki": "Helsinki"
}

# Tulostetaan sanakirja kokonaisuudessaan
print(henkilo)
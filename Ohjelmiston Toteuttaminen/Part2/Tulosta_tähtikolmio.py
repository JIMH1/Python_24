"""  Tehtävänanto

Kirjoita funktio tulosta_tähtikolmio, joka tulostaa kolmion muotoisen kuvion tähdillä, jossa on viisi riviä.
 """


def joulukuusi(korkeus):
    # Tulostetaan kuusen runko
    for i in range(korkeus):
        print(" " * (korkeus - i - 1) + "*" * (2 * i + 1))

# Määritä kuusen korkeus
korkeus = 5
joulukuusi(korkeus)
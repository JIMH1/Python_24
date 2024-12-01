"""  Tehtävänanto

Tässä tehtävässä sinulle on annettu valmiiksi lista nimistä. Tehtävänäsi on käsitellä tätä listaa eri tavoin käyttäen Pythonin listojen muokkausmetodeja. Opit lajittelun, alkioiden poistamisen ja lisäämisen listaan.

nimet = ["Matti", "Anna", "Liisa", "Jussi", "Kaisa"]
Vaiheet:

    Tulosta nimilista aakkosjärjestyksessä.
    Poista listasta tietty nimi.
    Lisää listaan uusi nimi ja tulosta päivitetty lista.

Vinkit:

    sort(): Tämä metodi lajittelee listan aakkosjärjestykseen. Voit käyttää sitä järjestääksesi nimilistan.
    remove(): Tällä metodilla voit poistaa listalta tietyn alkion (esim. poistetaan nimi 'Jussi').
    append(): Tämä metodi lisää uuden alkion listan loppuun (esim. lisätään uusi nimi 'Ville' listaan). """


nimet = ["Matti", "Anna", "Liisa", "Jussi", "Kaisa"]

# Tulostetaan nimilista aakkosjärjestyksessä
nimet.sort()
print("Aakkosjärjestyksessä:", nimet)

# Poistetaan nimi 'Jussi' listasta
nimet.remove("Jussi")
print("Poistettu 'Jussi':", nimet)

# Lisätään uusi nimi 'Ville' listaan ja tulostetaan päivitetty lista
nimet.append("Ville")
print("Lisätty 'Ville':", nimet)

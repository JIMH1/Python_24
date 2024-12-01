"""  Tehtävänanto

Tässä tehtävässä pääset käyttämään sanakirjoja (dictionaries) tallentaaksesi elokuvien nimiä ja niiden ilmestymisvuosia. Tehtävässä keskitytään tiedon tallentamiseen sanakirjaan ja tietyn tiedon hakemiseen sanakirjasta. Tämä auttaa sinua harjoittelemaan sanakirjojen avain-arvo-pareihin perustuvaa rakenteellista tietojen tallennusta sekä tietojen hakua.

Ohjeet:

    Sanakirjan luominen: Luo sanakirja nimeltä elokuvat, joka sisältää avain-arvo-pareja seuraavasti:
        Avain: Elokuvan nimi (merkkijonona, esim. "Titanic").
        Arvo: Elokuvan ilmestymisvuosi (kokonaislukuna, esim. 1997).

    Voit käyttää esimerkiksi seuraavia elokuvia ja ilmestymisvuosia:
        "Titanic": 1997
        "Gladiator": 2000
        "Inception": 2010
        "The Matrix": 1999
        "Pulp Fiction": 1994

    Tietyn elokuvan tiedon hakeminen: Kun olet luonut sanakirjan, tulosta tietyn elokuvan ilmestymisvuosi hakemalla arvo sanakirjasta sen avaimen perusteella. Valitse yksi elokuva sanakirjasta ja tulosta sen ilmestymisvuosi.


    Varmista virheettömyys: Huomioi, että sanakirjassa avaimet ovat merkkijonoja ja ne ovat case-sensitiivisiä, eli esimerkiksi "Titanic" ja "titanic" ovat eri avaimia. Muista käyttää täsmällistä avainta tietoa hakiessasi.

Tehtävän vaatimukset:

    Sanakirjan tulee sisältää vähintään viisi elokuvaa ja niiden ilmestymisvuotta.
    Tulosta yhden elokuvan ilmestymisvuosi suorittamalla haku sanakirjasta. """

  # Luodaan sanakirja
elokuvat = {'Titanic': '1997', 'Gladiator': '2000', 'Inception': '2010', 'The Matrix': '1999',  'Pulp Fiction': '1994'}

Leffa = elokuvat['Titanic'] # Sanakirjasta voi hakea arvoja

print(Leffa)


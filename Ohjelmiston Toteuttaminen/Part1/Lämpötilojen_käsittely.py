"""  Tehtävänanto
Sinulla on aiemmasta tehtävästä lista viikon keskilämpötiloista (Celsius-asteina). Kirjoita ohjelma, joka:

    Laskee viikon keskilämpötilan.
    Tulostaa viikon korkeimman ja matalimman lämpötilan.
    Lisää listaan uuden lämpötilan ja tulostaa päivitetyn listan.

Vihjeet:

    sum(lista): Laskee listan kaikkien arvojen summan. Esimerkiksi sum([1, 2, 3]) palauttaa arvon 6.
    len(lista): Palauttaa listan alkioiden määrän. Esimerkiksi len([1, 2, 3]) palauttaa arvon 3.
    max(lista): Palauttaa listan suurimman arvon. Esimerkiksi max([1, 2, 3]) palauttaa arvon 3.
    min(lista): Palauttaa listan pienimmän arvon. Esimerkiksi min([1, 2, 3]) palauttaa arvon 1.
 """

viikko_lampotila = {'15.5', '17.8', '14.2', '19.1', '18.7', '16.4', '20.3'}

print(viikko_lampotila)
print("minimi")
print(min([15.5, 17.8, 14.2, 19.1, 18.7, 16.4, 20.3, 10]))
print("maksimi")
print(max([15.5, 17.8, 14.2, 19.1, 18.7, 16.4, 20.3, 10]))
print("lukumäärä")
print(len([15.5, 17.8, 14.2, 19.1, 18.7, 16.4, 20.3, 10]))
print("summa")
print(sum([15.5, 17.8, 14.2, 19.1, 18.7, 16.4, 20.3, 10]))

keskilampotila = sum(viikko_lampotila) / len(viikko_lampotila)
print(f"Keskilämpötila: {keskilampotila:.2f}°C")

uusi_lampotila = 21
viikko_lampotila.append(uusi_lampotila)
print("Lisätty uusi", viikko_lampotila)

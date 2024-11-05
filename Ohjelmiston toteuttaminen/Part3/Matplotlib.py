"""  Tehtävänanto

    Asenna ja ota käyttöön Matplotlib aliaksella plt.
    Luo kaksi eri listaa, joita voit käyttää kaavion x-, ja y-akseleilla(esimerkki materiaaleissa).
    Visualisoi datasi Matplotlibin avulla luomalla yksinkertainen viivakaavio


pip install matplotlib """

import matplotlib.pyplot as plt

# Luodaan esimerkkidataa kahdelle listalle
x = [1, 2, 3, 4, 5]  # x-akselin arvot
y = [2, 4, 6, 8, 10]  # y-akselin arvot

# Luodaan yksinkertainen viivakaavio
plt.plot(x, y)

# Asetetaan otsikko ja akselien nimet
plt.title("Yksinkertainen viivakaavio")
plt.xlabel("X-akseli")
plt.ylabel("Y-akseli")

# Näytetään kaavio
plt.show()
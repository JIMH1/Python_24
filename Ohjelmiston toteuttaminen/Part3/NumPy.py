"""  Tehtävänanto

    Asenna NumPy kirjasto ja ota se käyttöön aliaksella np.
    Luo NumPy-taulukko.
    Laske sen keskiarvo ja summa.
    Tulosta molemmat.

pip install numpy
 """
import numpy as np

# Luodaan NumPy-taulukko
array = np.array([1, 2, 3, 4, 5])

# Lasketaan keskiarvo ja summa
keskiarvo = np.mean(array)
summa = np.sum(array)

# Tulostetaan tulokset
keskiarvo, summa

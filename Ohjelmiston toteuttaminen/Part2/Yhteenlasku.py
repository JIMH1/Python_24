"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjältä numeroita ja laskee niiden summan. Ohjelma lopettaa kysymisen, kun käyttäjä antaa luvun 0. """


# Alustetaan summa-muuttuja
summa = 0

while True:
    # Pyydetään käyttäjältä numeroa
    numero = int(input("Anna numero (0 lopettaa): "))
    
    # Tarkistetaan, onko annettu numero 0, jolloin silmukka lopetetaan
    if numero == 0:
        break
    
    # Lisätään annettu numero summaan
    summa += numero

# Tulostetaan kokonaissumma
print("Numeroiden summa on:", summa)

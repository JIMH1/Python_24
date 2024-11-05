"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjää syöttämään sanan ja tulostaa jokaisen merkin erikseen omalle rivilleen. """

# Pyydetään käyttäjää syöttämään sana
word = input("Syötä sana: ")

# Tulostetaan jokainen merkki omalle rivilleen
for char in word:
    print(char)
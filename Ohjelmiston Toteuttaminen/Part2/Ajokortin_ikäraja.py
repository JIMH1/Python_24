"""  Tehtävänanto

Kirjoita ohjelma, joka kysyy käyttäjän iän ja tarkistaa, onko hän tarpeeksi vanha saadakseen ajokortin (ikäraja 18 vuotta).

 """

age = 0
age = int(input("\nKerros ikäs\n"))
    
if age <= 17:
    print("oot alaikänen")
else:
    print("oot täysikäinen")

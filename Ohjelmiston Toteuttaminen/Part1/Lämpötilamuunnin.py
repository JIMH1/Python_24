"""  Tehtävänanto

Kirjoita ohjelma, joka pyytää käyttäjää syöttämään lämpötilan Celsius-asteina ja muuntaa sen Fahrenheit-asteiksi. Käytä kaavaa: F=C×95+32F = C \times \frac{9}{5} + 32

Tulosta muunnettu lämpötila.
 """

celsius = float(input("Anna lämpötila Celsius-asteina? "))
print(f"{celsius} astetta Celsiusta on { (celsius*1.8) + 32 } astetta Fahrenheit.")

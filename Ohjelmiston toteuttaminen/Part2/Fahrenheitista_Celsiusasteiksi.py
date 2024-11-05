"""  Tehtävänanto

Kirjoita funktio fahrenheit_to_celsius, joka ottaa parametrinä lämpötilan Fahrenheit-asteina ja palauttaa sen muunnettuna Celsius-asteiksi. """


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit_value = 100  
celsius_value = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value}°F on {celsius_value:.2f}°C")

""" 
Voit käyttää liitteenä olevaa todo-ohjelmaa pohjana, tai tehdä itse oman versiosi siitä.

Laajennusvaatimukset

    Tehtävälistan tallentaminen:
        Lisää sovellukseen toiminto, joka tallentaa kaikki tehtävälistassa olevat tehtävät todo.txt-tiedostoon.
        Jokainen tehtävä tulisi tallentaa tiedostoon omalle rivilleen.

    Tehtävälistan lataaminen:
        Lisää toiminto, joka lataa olemassa olevan tehtävälistan todo.txt-tiedostosta sovellukseen, kun ohjelma käynnistyy.
        Jos tiedostoa ei löydy, sovelluksen tulee luoda uusi tyhjä tiedosto tai jatkaa ilman virheilmoituksia.

    Käyttöliittymä:
        Lisää sovellukseen painike:
            "Tallenna tehtävät": tallentaa listan todo.txt-tiedostoon.

Vinkit

    Voit käyttää Pythonin open()-funktiota lukemaan ja kirjoittamaan tiedostoihin.
    Muista käsitellä tiedoston lukemis- ja kirjoitusvirheet try-except -rakenteella.
    Mieti, missä kohtaa ohjelmaa lataustoiminto olisi järkevintä tehdä, jotta käyttäjä näkee aiemmat tehtävänsä heti ohjelman avattuaan.
 """

import os
import tkinter as tk
from tkinter import messagebox

# Tiedoston nimi
TODO_FILE = 'todo.txt'

# Funktio tehtävien tallentamiseen tiedostoon
def tallenna_tehtavat():
    with open(TODO_FILE, 'w') as file:
        for tehtava in tehtavalista.get(0, tk.END):
            file.write(tehtava + '\n')
    messagebox.showinfo("Tallennettu", "Tehtävät on tallennettu tiedostoon.")

# Funktio tehtävien lataamiseen tiedostosta
def lataa_tehtavat():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            for line in file:
                tehtavalista.insert(tk.END, line.strip())
    else:
        # Luodaan uusi tyhjä tiedosto, jos sitä ei ole
        open(TODO_FILE, 'w').close()

# Funktio yhden tehtävän poistamiseen
def poista_tehtava():
    try:
        valittu_indeksi = tehtavalista.curselection()[0]
        tehtavalista.delete(valittu_indeksi)
    except IndexError:
        messagebox.showwarning("Ei valintaa", "Valitse ensin poistettava tehtävä.")
        
# Funktio tehtävälistan nollaamiseen
def tyhjenna_lista():
    tehtavalista.delete(0, tk.END)
    tallenna_tehtavat()
    messagebox.showinfo("Tyhjennetty", "Kaikki tehtävät on poistettu.")

# Funktio tehtävän lisäämiseen listaan
def lisaa_tehtava():
    tehtava = tehtava_entry.get()
    if tehtava:
        tehtavalista.insert(tk.END, tehtava)
        tehtava_entry.delete(0, tk.END)

# Graafinen käyttöliittymä
root = tk.Tk()
root.title("Tehtävälista")

# Ladataan tehtävät sovelluksen käynnistyessä
lataa_tehtavat()

# Tekstikenttä tehtävän lisäämiselle
tehtava_entry = tk.Entry(root, width=50)
tehtava_entry.pack(pady=10)

# Painike tehtävän lisäämiselle listaan
lisaa_button = tk.Button(root, text="Lisää tehtävä", command=lisaa_tehtava)
lisaa_button.pack()

# Tehtävälista (Listbox)
tehtavalista = tk.Listbox(root, width=50, height=10)
tehtavalista.pack(pady=10)

# "Tallenna tehtävät" -painike
tallenna_button = tk.Button(root, text="Tallenna tehtävät", command=tallenna_tehtavat)
tallenna_button.pack(pady=5)

# "Poista yksi tehtävä" -painike
poista_button = tk.Button(root, text="Poista yksi tehtävä", command=poista_tehtava)
poista_button.pack(pady=5)

# "Tyhjennä kaikki" -painike
tyhjenna_button = tk.Button(root, text="Tyhjennä kaikki", command=tyhjenna_lista)
tyhjenna_button.pack(pady=5)

# Käynnistä pääsilmukka
root.mainloop()


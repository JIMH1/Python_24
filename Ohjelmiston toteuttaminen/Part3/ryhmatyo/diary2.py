from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import base64
import os

import subprocess
import sys

# Function to install a package
def install_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} has been installed successfully.")

# Check and install the 'cryptography' package
install_package("cryptography")

# Now you can import and use cryptography in your code
from cryptography.fernet import Fernet 

# Example usage of cryptography
key = Fernet.generate_key()
cipher = Fernet(key)
print("Cryptography library is ready to use.")

# Initialize the main window
root = Tk()
root.title('Kirjoituskone')
root.geometry("820x620")

# Initialize global variables for file status
global avoin_status
avoin_status = False
global valittu
valittu = False

# Generate a Fernet object using a password
def get_fernet(password):
    key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
    return Fernet(key)

# Functions for file operations
def uusi_tiedosto():
    minun_teksti.delete("1.0", END)
    global avoin_status
    avoin_status = False
    status_bar_left.config(text="Uusi tiedosto\t")

# Open file function with decryption
def avaa_tiedosto():
    minun_teksti.delete("1.0", END)
    teksti_tiedosto = filedialog.askopenfilename(initialdir="C:/", title="Avaa tiedosto", filetypes=(("Tekstitiedostot", "*.txt"), ("Kaikki tiedostot", "*.*")))
    
    if teksti_tiedosto:
        global avoin_status
        avoin_status = teksti_tiedosto
        password = simpledialog.askstring("Salasana", "Syötä salasanasi tiedoston avaamiseksi:", show="*")
        if password:
            fernet = get_fernet(password)
            try:
                with open(teksti_tiedosto, 'rb') as tiedosto:
                    encrypted_text = tiedosto.read()
                    sisältö = fernet.decrypt(encrypted_text).decode()
                    minun_teksti.insert(END, sisältö)
                    status_bar_left.config(text=f'{teksti_tiedosto}\t')
            except Exception as e:
                messagebox.showerror("Virhe", "Salasana on väärä tai tiedosto on korruptoitunut.")
        else:
            messagebox.showwarning("Salasana vaaditaan", "Anna salasana avataksesi tiedoston")

# Save As function with encryption
def tallenna_nimellä():
    teksti_tiedosto = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Tallenna tiedosto", filetypes=(("Tekstitiedostot", "*.txt"), ("Kaikki tiedostot", "*.*")))
    
    if teksti_tiedosto:
        password = simpledialog.askstring("Salasana", "Syötä salasana tiedoston tallentamiseksi:", show="*")
        if password:
            fernet = get_fernet(password)
            text = minun_teksti.get("1.0", END).encode()
            encrypted_text = fernet.encrypt(text)
            with open(teksti_tiedosto, 'wb') as tiedosto:
                tiedosto.write(encrypted_text)
            status_bar_left.config(text=f'Tallennettu: {teksti_tiedosto}\t')
            global avoin_status
            avoin_status = teksti_tiedosto
            messagebox.showinfo("Onnistui", "Tiedosto on tallennettu salatusti.")
        else:
            messagebox.showwarning("Salasana vaaditaan", "Anna salasana tallentaaksesi tiedoston.")

# Save function
def tallenna_tiedosto():
    global avoin_status
    if avoin_status:
        password = simpledialog.askstring("Salasana", "Syötä salasana tallentaaksesi tiedoston:", show="*")
        if password:
            fernet = get_fernet(password)
            text = minun_teksti.get("1.0", END).encode()
            encrypted_text = fernet.encrypt(text)
            with open(avoin_status, 'wb') as tiedosto:
                tiedosto.write(encrypted_text)
            status_bar_left.config(text=f'Tallennettu: {avoin_status}\t')
            messagebox.showinfo("Onnistui", "Tiedosto on tallennettu salatusti.")
    else:
        tallenna_nimellä()

# Text editing functions
def leikkaa_teksti():
    global valittu
    if minun_teksti.selection_get():
        valittu = minun_teksti.selection_get()
        minun_teksti.delete("sel.first", "sel.last")

def kopioi_teksti():
    global valittu
    if minun_teksti.selection_get():
        valittu = minun_teksti.selection_get()

def liitä_teksti():
    if valittu:
        positio = minun_teksti.index(INSERT)
        minun_teksti.insert(positio, valittu)

# Status bar updater
def paivita_status(event=None):
    line, column = minun_teksti.index(INSERT).split('.')
    total_lines = int(minun_teksti.index('end-1c').split('.')[0])
    total_chars = len(minun_teksti.get("1.0", 'end-1c'))
    status_bar.config(text=f'Merkkejä: {total_chars}, Rivejä: {total_lines}\tLn: {line}, Col: {int(column)+1}\t')

# Frame and scrollbar for text
minun_frame = Frame(root)
minun_frame.pack(fill=BOTH, expand=True, pady=5)

tekstin_rullaus = Scrollbar(minun_frame)
tekstin_rullaus.pack(side=RIGHT, fill=Y)

minun_teksti = Text(minun_frame, width=98, font=("helvetica", 16), selectbackground="blue", selectforeground="black", undo=True, yscrollcommand=tekstin_rullaus.set)
minun_teksti.pack(side=LEFT, fill=BOTH, expand=True)
tekstin_rullaus.config(command=minun_teksti.yview)

# Bind events to update status bar
minun_teksti.bind('<KeyRelease>', paivita_status)
minun_teksti.bind('<ButtonRelease>', paivita_status)

# Menu setup
minun_valikko = Menu(root)
root.config(menu=minun_valikko)

# File menu
tiedosto_valikko = Menu(minun_valikko, tearoff=False)
minun_valikko.add_cascade(label="Tiedosto", menu=tiedosto_valikko)
tiedosto_valikko.add_command(label="Uusi", command=uusi_tiedosto)
tiedosto_valikko.add_command(label="Avaa", command=avaa_tiedosto)
tiedosto_valikko.add_command(label="Tallenna", command=tallenna_tiedosto)
tiedosto_valikko.add_command(label="Tallenna nimellä", command=tallenna_nimellä)
tiedosto_valikko.add_separator()
tiedosto_valikko.add_command(label="Poistu", command=root.quit)

# Edit menu
muokkaus_valikko = Menu(minun_valikko, tearoff=False)
minun_valikko.add_cascade(label="Muokkaa", menu=muokkaus_valikko)
muokkaus_valikko.add_command(label="Leikkaa", command=leikkaa_teksti)
muokkaus_valikko.add_command(label="Kopioi", command=kopioi_teksti)
muokkaus_valikko.add_command(label="Liitä", command=liitä_teksti)
muokkaus_valikko.add_command(label="Kumoa", command=minun_teksti.edit_undo)
muokkaus_valikko.add_command(label="Tee uudelleen", command=minun_teksti.edit_redo)

# Status bar
status_frame = Frame(root)
status_frame.pack(fill=X, side=BOTTOM)
status_bar_left = Label(status_frame, text='', anchor=SW)
status_bar_left.pack(side=LEFT)
status_bar = Label(status_frame, text='Valmis\t', anchor=SE)
status_bar.pack(side=RIGHT)

# Run the main loop
root.mainloop()

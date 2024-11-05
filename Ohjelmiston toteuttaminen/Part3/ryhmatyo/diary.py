import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from cryptography.fernet import Fernet
import base64
import os

class SecureTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("suojattu muistio")
        
        # tekstialueen asetukset
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)
        
        # tallennuksen ja avaamisen napit
        save_button = tk.Button(root, text="Tallenna", command=self.save_encrypted)
        save_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        load_button = tk.Button(root, text="Avaa", command=self.load_encrypted)
        load_button.pack(side=tk.RIGHT, padx=10, pady=10)

# tekstin tallennuksen alue
    def save_encrypted(self):
        password = simpledialog.askstring("Salasana", "anna salasanai", show="*")
        if password:
            fernet = self.get_fernet(password)
            text = self.text_area.get("1.0", tk.END).encode()
            encrypted_text = fernet.encrypt(text)
            with open("secure_notes.enc", "wb") as file:
                file.write(encrypted_text)
            messagebox.showinfo("Onnistuit", "tekstisi tallennettu")
        else:
            messagebox.showwarning("Salasana tarvitaan", "Annas Salasansi")
# tekstin avaamisen runko
    def load_encrypted(self):
        if not os.path.exists("secure_notes.enc"):
            messagebox.showwarning("Tiedosto uupuu")
            return

        password = simpledialog.askstring("Salasana", "vaaditaan tiedoston avaamiseen:", show="*")
        if password:
            fernet = self.get_fernet(password)
            try:
                with open("secure_notes.enc", "rb") as file:
                    encrypted_text = file.read()
                    decrypted_text = fernet.decrypt(encrypted_text).decode()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, decrypted_text)
                messagebox.showinfo("Tiedosto", "on avattuna")
            except Exception as e:
                messagebox.showerror("Decryption Failed", "Incorrect password or corrupted file.")
        else:
            messagebox.showwarning("Salasana vaaditaan", "Anna salasani avaaksesi tiedoston")
# suojaus
    @staticmethod
    def get_fernet(password):
        key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
        return Fernet(key)

# varsinainen moottori
root = tk.Tk()
app = SecureTextApp(root)
root.mainloop()

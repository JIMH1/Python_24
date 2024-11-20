import subprocess
import sys
import base64
import os

# Function to install a package
def install_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} has been installed successfully.")

# This module can be used to create the hash and salt text file for a given password.
# Set the password and url and run this script.
# Use the generated file in the text editor.
#
# TES, 13.11.2024

# Can be used to save the salt and password hash into a given file:
#
# url       the full path of the file to save to
# password  the password to hash
#
def save_password_to_file(url, password):
    bytes = password.encode('utf-8') 
    salt = bcrypt.gensalt() 
    hash = bcrypt.hashpw(bytes, salt) 
    file = open(url, "w")
    file.write(hash.decode('utf-8') + "\n")
    file.write(salt.decode('utf-8'))

# Can be used to login to the app. Requires that the password and salt are saved in a 
# text file already on different rows. First the hash of the password and the salt and
# then the salt.
#
# url       the full path of a text file where the password hash and salt are
# password  the password the user has given to try to login
#
# returns: true - if the login was ok
#          false - if password doesn't match
#
def login(url, password):
    file = open(url, "r")
    hash = file.readline().encode('utf-8').strip()
    salt = file.readline().encode('utf-8')
    bytes = password.encode('utf-8') 
    hash2 = bcrypt.hashpw(bytes, salt) 
    print(hash.decode('utf-8'))
    print(hash2.decode('utf-8'))
    return hash == hash2

# Make sure the bcrypt package is installed:
install_package("bcrypt")

import bcrypt

# Set the password here:
password = "d34fgi8"

# Set the url to save to here:
url = "password_hash.txt"

# Generates the hash using a salt and saves both into a text file:
save_password_to_file("password_hash.txt", password)

# This code was used to test that the login fails for a wrong password and works for a correct password:
#
# print(login(url, "assword7865"))
# print(login(url, "password7865"))


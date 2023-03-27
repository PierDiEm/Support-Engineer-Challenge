# Write a python or bash script that takes three parameters, two strings and a directory
# name, and substitutes any occurrence of the first string with the second string for any file
# in the directory, recursively




import os
import re


# Base solution for exercise 1
def sostituisci_in_file_base(stringa1, stringa2, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                contenuto = f.read()
            contenuto = contenuto.replace(stringa1, stringa2)
            with open(path, 'w') as f:
                f.write(contenuto)

                
#  Extended solution with error handling
def sostituisci_in_file_gestione_errore(stringa1, stringa2, directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                # Ignoriamo eventuali link simbolici e file di sola lettura
                if os.path.islink(path) or not os.access(path, os.W_OK):
                    continue
                with open(path, 'r') as f:
                    contenuto = f.read()
                if stringa1 in contenuto:
                    # Usiamo una regex per trovare tutte le occorrenze di stringa1 nel file
                    regex = re.compile(re.escape(stringa1), re.IGNORECASE)
                    nuovo_contenuto = regex.sub(stringa2, contenuto)
                    with open(path, 'w') as f:
                        f.write(nuovo_contenuto)
    except OSError:
        print(f"Errore: impossibile accedere alla directory {directory}.")               

# Write a python or bash script that counts the number of script files in a directory subdividing
# it by the shebang interpreter.


import os
import mimetypes
import subprocess
import glob




# Directory da controllare
directory = '/percorso/directory'

# Contatore dei file di script
script_count = 0

# Loop attraverso tutti i file nella directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    # Verifica se il file è un file di script
    if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
        with open(filepath, 'r') as f:
            first_line = f.readline().strip()
            # Verifica se la prima riga del file contiene l'interprete shebang
            if first_line.startswith('#!'):
                script_count += 1

# Stampa il numero di file di script trovati
print(f"Numero di file di script trovati nella directory {directory}: {script_count}")






# Seconda risoluzione con la gestione di alcuni casi specifici
def count_script_files(directory):
    """
    Conta il numero di file di script nella directory specificata
    utilizzando l'interprete shebang.
    """
    # Contatore dei file di script
    script_count = 0

    # Pattern di ricerca dei nomi di file con l'interprete shebang
    pattern = os.path.join(directory, '*')
    files = glob.glob(pattern)

    # Loop attraverso i file che soddisfano il pattern di ricerca
    for filepath in files:
        # Verifica se il file è un file di testo
        file_type, encoding = mimetypes.guess_type(filepath)
        if not file_type or not file_type.startswith('text/'):
            continue

        # Verifica se il file è eseguibile e ha un'interprete shebang
        if os.access(filepath, os.X_OK):
            with open(filepath, 'r') as f:
                first_line = f.readline().strip()
                # Verifica se la prima riga del file contiene l'interprete shebang
                if first_line.startswith('#!'):
                    # Verifica se l'interprete specificato nell'interprete shebang esiste
                    interpreter = first_line[2:].strip()
                    try:
                        subprocess.call(['which', interpreter], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    except subprocess.CalledProcessError:
                        continue
                    script_count += 1

    return script_count

# Directory da controllare
directory = '/percorso/directory'

# Conta il numero di file di script nella directory
script_count = count_script_files(directory)

# Stampa il numero di file di script trovati
print(f"Numero di file di script trovati nella directory {directory}: {script_count}")

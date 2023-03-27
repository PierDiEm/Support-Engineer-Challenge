# Spiegazione Esericizio 2


## Soluzione Base
Nella prima risoluzione ho creato questo script dove si  specifica la directory da controllare nel primo parametro `directory`.  Si itera attraverso tutti i file nella directory e si verifica se ogni file è un file di script tramite la funzione `os.access()` che controlla se il file è eseguibile `(os.X_OK)`.
Successivamente, si apre ogni file e si verifica se la prima riga del file contiene l'interprete shebang con la condizione `if first_line.startswith('#!')`. Se la condizione è vera, incrementiamo il contatore dei file di script `script_count`.
Infine, si stampa il numero di file di script trovati nella directory specificata.

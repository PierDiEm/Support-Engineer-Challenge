# Spiegazione Esericizio 2


## Soluzione Base
Nella prima risoluzione ho creato questo script dove si  specifica la directory da controllare nel primo parametro `directory`.  Si itera attraverso tutti i file nella directory e si verifica se ogni file è un file di script tramite la funzione `os.access()` che controlla se il file è eseguibile `(os.X_OK)`.
Successivamente, si apre ogni file e si verifica se la prima riga del file contiene l'interprete shebang con la condizione `if first_line.startswith('#!')`. Se la condizione è vera, incrementiamo il contatore dei file di script `script_count`.
Infine, si stampa il numero di file di script trovati nella directory specificata.


##  Soluzione con gestione casi specifici
Nella seconda risoluzione ho voluto:
- Aggiungere un controllo per verificare se il file è un file di testo, poiché la lettura di file binari può causare errori. Questo può essere fatto verificando se il tipo di file è `file` e se il tipo MIME del file è `text/*`.
- Ho scelto di utilizzare la libreria `glob` invece di `os.listdir()` per ottenere solo i file di script nella directory. Questo ci consente di specificare il pattern di ricerca dei nomi di file con l'interprete shebang e di evitare di dover iterare attraverso i file che non soddisfano il pattern.
- Ho utilizzato la funzione `subprocess.call()` per verificare se l'interprete specificato nell'interprete shebang esiste effettivamente nel sistema. In questo modo evitiamo di contare i file che hanno un'interprete shebang non valido o che fa riferimento a un interprete che non è installato nel sistema.
- Infine ho scelto di rendere lo script più modulare e riutilizzabile portando fuori il conteggio dei file di script in una funzione separata.

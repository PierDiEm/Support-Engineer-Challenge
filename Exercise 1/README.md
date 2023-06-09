#  Spiegazione Esercizio 1


## Soluzione Base
Nella prima risoluzione (base) ho creato uno script in Python che, prendendo tre parametri in input (due stringhe e una directory), attraversa ricorsivamente la directory e sostituisce, per tutti i file della `directory`, la `stringa1` con la `stringa2`.
Il metodo `os.walk(directory)` attraversa in modo ricorsivo la directory e le sue sottodirectory, restituendo una tupla `(root, dirs, files)` per ogni directory incontrata. `root` è la directory corrente che viene attraversata, `dirs` è una lista di sottodirectory in root e `files` è una lista di file in root. Iteriamo sulla lista files e leggiamo il contenuto di ogni file usando `open(path, 'r')`. Sostituiamo quindi qualsiasi occorrenza di `stringa1` con `stringa2` usando il metodo `replace()` della classe `str` e scriviamo il contenuto modificato di nuovo nel file usando `open(path, 'w')`.


## Soluzione con gestione errori
Nella seconda risoluzione (gestione errore) ho voluto implementare la risoluzione base con la gestione di alcuni errori che si potrebbero presentare: 
- La directory non esiste o non è accessibile
- La directory contiene link simbolici o file di sola lettura
- La prima stringa non viene trovata in un file
- La seconda stringa viene usata per sostituire la prima stringa in modo errato, ad esempio se la seconda stringa è una sottostringa della prima stringa.

Per gestire il caso in cui la directory non esiste o non è accessibile ho integrato un blocco try - except. Per gestire i link  simbolici e file di sola lettura nella directory ho aggiunto la linea di codice 31 dove la funzione `os.path.islink()` restituisce `True` se il path argument punta a un link simbolico, altrimenti restituisce `False`. La funzione `os.access()` controlla se l'utente corrente ha i diritti di accesso specificati per il file/directory al percorso dato. Il secondo argomento `os.W_OK` specifica che stiamo verificando se l'utente ha il permesso di scrittura. Se l'utente ha il permesso di scrittura, `os.access()` restituisce `True`, altrimenti restituisce `False`. Se `os.path.islink()` restituisce `True` o `os.access()` restituisce `False`, l'istruzione continue salta l'iterazione corrente del ciclo e procede alla successiva. Ciò significa che il blocco di codice che segue questo frammento non verrà eseguito per i path che sono link simbolici o per cui l'utente non ha il permesso di scrittura.
Inoltre, ho usato una `regex` per trovare tutte le occorrenze di stringa1 nel file, in modo da evitare problemi se la seconda stringa è una sottostringa della prima stringa. Infine, ho aggiunto il flag `re.IGNORECASE` alla regex, in modo da ignorare la differenza tra lettere maiuscole e minuscole durante la ricerca.

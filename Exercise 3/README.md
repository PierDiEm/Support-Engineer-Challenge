# Spiegazione Esercizio 3


## Stringa cron
La stringa cron è composta da 5 campi separati da uno spazio e il loro significato è il seguente:
- `0` (minuto): specifica il minuto dell'ora in cui l'azione deve essere eseguita (in questo caso, `0` indica che l'azione deve essere eseguita all'inizio dell'ora).
- `0` (ora): specifica l'ora del giorno in cui l'azione deve essere eseguita (in questo caso, `0` indica la mezzanotte).
- `*` (giorno del mese): specifica il giorno del mese in cui l'azione deve essere eseguita (in questo caso, `*` indica che l'azione deve essere eseguita ogni giorno del mese).
- `*` (mese): specifica il mese in cui l'azione deve essere eseguita (in questo caso, `*` indica che l'azione deve essere eseguita ogni mese).
- `0` (giorno della settimana): specifica il giorno della settimana in cui l'azione deve essere eseguita (in questo caso, `0` indica la domenica).

## Azione eseguita ogni domenica
L'azione eseguita ogni domenica notte è composta da due parti separate da &&:
- La prima parte crea un file di backup compresso `backup.tar.gz` della cartella `/home/user` utilizzando il comando `tar`.
- La seconda parte invia il file di backup al server remoto utilizzando il comando `ssh`. Il comando `mkdir -p /remote/backup/location` crea la directory di destinazione sul server remoto, se non esiste già. Successivamente, il comando `cat > /remote/backup/location/backup.tar.gz` riceve i dati del file di backup dalla pipe standard input (cioè il file `/home/user/backup.tar.gz`) e li scrive nel file `backup.tar.gz` nella directory di destinazione sul server remoto.

La stringa cron assume che la chiave pubblica sia stata installata correttamente sul server remoto per l'utente `user`. Inoltre, è possibile specificare opzioni aggiuntive per il comando `ssh`, come la porta remota, l'autenticazione tramite chiave privata e la compressione dei dati durante il trasferimento.

# Risoluzione esercizio 4

L'architettura della soluzione proposta prevede l'utilizzo di Terraform per la creazione dell'infrastruttura su AWS e di Ansible per la configurazione dei server. L'applicazione WordPress verrà eseguita su un'istanza EC2 con un'immagine Amazon Linux 2 e Nginx come server web.

## Requisiti
- AWS account
- Terraform
- Ansible

## Istruzioni
- Configurare le variabili di ambiente: impostare le variabili di ambiente necessarie per il progetto, come l'accesso alle chiavi AWS e il nome del bucket S3.

```
ssh-keygen -t rsa -b 4096 -f ./deployer-key
```

Aggiungere la chiave pubblica `deployer-key.pub` come chiave di accesso alla propria area di lavoro AWS.

- Creare l'infrastruttura con Terraform: eseguire il comando Terraform per creare l'infrastruttura AWS necessaria, come l'istanza EC2, il gruppo di sicurezza, il bilanciamento del carico e il bucket S3.

```
aws_access_key = "your_aws_access_key"
aws_secret_key = "your_aws_secret_key"
aws_region = "your_aws_region"
instance_type = "t2.micro"
ami = "ami-0c55b159cbfafe1f0"
wordpress_version = "latest"
```

Nei campi `your_aws_access_key`, `your_aws_secret_key`, `your_aws_region` bisogna inserire le proprie credenziali AWS e la regione in cui si vuole creare l'infrastruttura. Si puo scegliere l'immagine AMI che preferisci, assicurandoti che sia compatibile con l'istanza EC2 selezionata.

- Creare l'infrastruttura con Terraform: eseguire il comando Terraform per creare l'infrastruttura AWS necessaria, come l'istanza EC2, il gruppo di sicurezza, il bilanciamento del carico e il bucket S3.

```
terraform init
terraform apply
```

Questo comando creerà tutte le risorse necessarie su AWS (VPC, subnet, security group, istanza EC2).

- Configurare l'istanza EC2: utilizzando Ansible, configura l'istanza EC2 appena creata installando e configurando Nginx e WordPress.

```
ansible-playbook -i hosts.yml playbook.yml
```

- Accedere al sito WordPress

Dopo aver completato la configurazione, si può accedere al sito WordPress all'indirizzo IP pubblico dell'istanza EC2. Per connettersi al pannello di amministrazione di WordPress, basterà andare su `http://<indirizzo_ip>/wp-admin` e accedere con le credenziali predefinite (`admin` come nome utente e `password` come password).

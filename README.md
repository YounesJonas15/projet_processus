## Installation des dependancies

Un fichier requirement.txt est à votre disposition, tout ce que vous avez à faire est de lancer la commande: 
```pip install -r requirements.txt```

Pour les 2 application web, il est nécessaires de lancer la commande ```npm install``` dans les 2 dossiers application client et validation_commande.

## Lancement du projet
A fin de tester le produit, il est nécessaire de lancer tout ce qui suit en utilisant les bonnes commandes: 

1. Dossier validation_commande, lancez la commande ```node index.js``` pour lancer l'appli web.
2. Dossier application client, lancez la commande ```node index.js``` pour lancer l'appli web.
3. Dossier App, lancez la commande ```python fournisseur.py``` pour lancer le serveur fournisseur.
4. Dossier App, lancez la commande ```python placerCommande.py``` pour lancer le serveur placerCommande.
5. Dossier App, lancez la commande ```python worker_verification.py``` pour lancer le premier worker.
6. Dossier App, lancez la commande ```python worker_fin_verif.py``` pour lancer le deuxième worker.

## Utilisation
L'ajout d'une nouvelle commande se fait dans l'application client, ou celui-ci peut aussi valider son devis après que le fournisseur l'ai généré.
Pour le fournisseur, dans l'application validation commande, il peut valider les commandes de ses client tout en générant directement leur devis.

## Contact
Pour toutes questions supplémentaire, n'hésitez pas à nous contacter: 
M.Yassine : mazizyassine25@gmail.com
A.Younes: younesamrane01@gmail.com

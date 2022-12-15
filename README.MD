# Demonstration d'une authentification via un token JWT, et gestion des MDP chiffrés

Ce serveur web tourne en Python avec le framework Flask.
Trois web services permettent d'intéragir avec le serveur :

- http://localhost:5000/rest/register/user (permet d'enregistrer un nouvel utilisateur)
- http://localhost:5000/rest/auth/user (permet de s'authentifier pour obtenir un token JWT)
- http://localhost:5000/rest/get/books (permet aux utilisateurs authentifiés de récupérer la liste des livres enregistrés)

## Installation
1. Installer Python 3.X
2. Installer MariaDB (dernière version)
3. `git clone https://github.com/KaeLCe/DEMO_CESI.git` (l'utilitaire git va télécharger le code et le placer là où vous lancez la commande. Sous Windows utilisez l'invite de commande Git Bash)
4. Avec un client SQL (HeidiSQL par exemple), importez la BDD avec le fichier script.sql (le script va créer la base de donnée et l'utilisateur de BDD qui sera utilisé par le serveur Python, celui que l'on retrouve dans le fichier config.json. Celui-ci dispose de droit restreint.)
5. Dans votre invite de commande, lancez les commandes suivantes :
    - `pip install flask`
    - `pip install pyjwt`
    - `pip install bcrypt`
    - `pip install mariadb`
6. Positionnez vous dans le répertoire contenant le fichier main.py : `cd DEMO_CESI`
6. Lancez le serveur avec la commande `python main.py`

Par défaut, un utilisateur est déjà créé : **toto // coucou123**

## Requêtes Curl
- `curl -X POST -H 'Content-Type: application/json' -d '{"login": "test": "password": "mdp"}' http://localhost:5000/rest/register/user`
- `curl -X POST -H 'Content-Type: application/json' -d '{"login": "test": "password": "mdp"}' http://localhost:5000/rest/auth/user`
- `curl -X GET -H 'Authorization: Bearer [le_token_jwt]' http://localhost:5000/rest/get/books`[^1]

[^1]: Ne pas mettre les crochets [ ] autour du JWT, et pensez à ajouter le mot clef **Bearer** suivi d'un espace devant le token JWT. Le token à renseigner est celui que l'on obtient avec la requête d'authentification.

## Exercice
Pour les plus motivés, essayez de modifier via la plateforme jwt.io un token obtenu, et rejouez la 3ème requêtes pour obtenir la liste des livres, avec ce token modifié. Vous constaterez alors le principe d'un token **scellé**.

## Commentaires
- Le code se veut fonctionnel, il s'agit d'une démo et non d'un code à faire tourner en production. En l'occurence, on ne met jamais le script.sql de la BDD et le fichier de configuration dans le dépôt de code. Mais pour vous simplifier l'installation, j'ai tout mis dedans.
- Pour fonctionner, la base de donnée doit tourner sur la même machine que celle qui fait tourner le serveur web, et doit être exposée sur le port 3306. Vous pouvez changer le port et l'adresse de la BDD dans le fichier config.json si besoin, mais si elle tourne sur une autre machine vous devrez modifier le script SQL pour la création de l'utilisateur dédié (qui en l'état n'est autorisé à communiquer avec la BDD qu'en localhost).
- Pour ceux qui souhaitent lire le code, je vous recommande d'ouvrir le répertoire avec Visual Studio Code. L'IDE vous proposera potentiellement (s'il n'y est pas par défaut) d'installer un plugin Python pour faire la coloration syntaxique, ce qui rendra la lecture nettement plus agréable. A défaut, Github fait la coloration syntaxique pour les plus fénéants.

Si vous avez des question je reste dispo :wink:

:email: lecroller@hotmail.fr | kevin.lecroller@3s-securite.eu | ou Discord






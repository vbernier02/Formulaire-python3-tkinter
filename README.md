TP : Formulaire d'Identification Sécurisé
Auteur: Vincent BERNIER

--Informations Techniques--

Prérequis
- python/python3
- tkinter
- SQLite3

Dépendances
- tkinter
- sqlite3
- hashlib
- os

Technologie
- Language : python
- Interface Graphique : tkinter
- Base de données : SQLite3
- Sécurité : hachage SHA-256 des mots de passe des profils

--Utilisation--

Execution
- python3 Formulaire.py
remarque : Le fichier `logop8.png` doit être dans le même répertoire

Test
-Pour utiliser le formulaire, il est nécessaire de créer un profil au préalable avec le bouton créer un compte (il est possible d'utiliser la paire identifier/mot de passe test/test pour vérifier la connexion)

--Implémentation--
L'application affiche un formulaire d'identification avec les éléments suivantes :

Fenêtre Principale avec :
- Un premier champ pour un "Identifiant"
- Un second champ pour un "mot de passe"
- 3 boutons :
      - bouton "connexion" pour vérifier les informations (raccourcis : touche entrée)
      - bouton "Créer un compte" ouvrir une fenêtre d'inscription
      - bouton "Reset" qui vide tous les champs du formulaire

Fenêtre d'inscription avec :
- Un premier champ pour un "Identifiant"
- Un second champ pour un "mot de passe"
- Un troisième champ pour la confirmation du mot de passe
- 2 boutons :
      - bouton "créer le compte" pour créer un profils identifiant/mot de passe une fois tout les champs correctement remplie
      - bouton "retour" pour fermer la fenêtre d'inscription 

Gestion de base de données avec SQLite
- Création d'un fichier data_user.db même répertoire que le code source
- Le fichier contient une table "users" avec les colonnes suivantes :
      - "id" : Identifiant unique
      - "username" : Identifiant choisie par l'utilisateur
      - "password_hash" : Mot de passe choisie par l'utilisateur haché en SHA-256

--Sécurité--
- Les mots de passe sont hachés avec SHA-256
- Les mots de passe ne s'affichent pas à l'écran

--Identifiant/mot de passe--
Compte test prêt à l'usage
      identifiant  : test
      mot de passe : test 

--Exécution--
- python3 Formulaire.py
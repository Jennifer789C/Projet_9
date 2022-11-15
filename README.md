# OpenClassRooms - Python - Projet 9 : LITReview

Ce projet consiste à créer un blog de partage de critiques littéraires :  
<!-- 2 espaces à la fin de la ligne pour un saut de ligne -->
	- utilisation du framework Django,
	- mise en place de gabarits partiels,  
	- mise en place de filtres et de balises personnalisés,  
	- mise en place d'un CustomUser (modèle d'utilisateur personnalisé),  
    - utilisation d'une table intermédiaire pour une relation ManyToMany,  
    - mise en place d'un système d'abonnement entre utilisateur.


## Application du script

A partir du terminal, se placer dans le répertoire souhaité

### 1. Récupérer le repository GitHub et créer un environnement virtuel

Cloner le repository GitHub :
```bash
git clone https://github.com/Jennifer789C/Projet_9.git
```
Puis se placer dans le répertoire du projet :
```bash
cd Projet_9
```
*Pour ma part, je travaille sous Windows et avec l'IDE PyCharm, la création d'un environnement virtuel se fait via les paramètres de l'IDE*

Depuis un terminal sous Windows :
```bash
python -m venv env
env/Scripts/activate
```

Depuis un terminal sous Linux ou Mac :
```bash
python3 -m venv env
source env/bin/activate
```


### 2. Ouvrir le site et le parcourir

Se placer dans le répertoire du projet Django :
```bash
cd LITReview
```
Lancer le script python :
```bash
python manage.py runserver
```
Ouvrir la page HTML et la parcourir

### 3. Détails de connexion des utilisateurs déjà inscrits

Quatre utilisateurs sont déjà inscrits et présents dans la base de données :  

    - un superuser : 
        * username : Admin  
        * mot de passe : mdpAdmin  
        * abonné à : matt_51 & mimi.bebe  
        * suiveurs : mimi.bebe & jenny@789

    - un 1er utilisateur :  
        * username : jenny@789  
        * mot de passe : mdpuser1  
        * abonné à : matt_51 & Admin  
        * suiveurs : néant

    - un 2e utilisateur :  
        * username : matt_51  
        * mot de passe : mdpuser2  
        * abonné à : néant  
        * suiveurs : Admin & jenny@789 

    - un 3e utilisateur :  
        * username : mimi.bebe  
        * mot de passe : mdpuser3  
        * abonné à : Admin  
        * suiveurs : Admin
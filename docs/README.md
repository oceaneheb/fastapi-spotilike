# fastapi-spotilike

## Pré-requis 
Avant de lancer le projet, assurez-vous d'avoir installé les logiciels suivants sur votre ordinateur :
- Python
- Node.js

## Lancement de l'API
1. Ouvrir un terminal, se rendre dans le dossier API et créer un environnement virtuel Python :
```
cd API
py -m venv venv
```
2. Activer l'environnement virtuel Python :
```
.\venv\Scripts\activate
```
3. Installer les dépendances nécessaires :
```
pip install -r requirements.txt
```
4. Lancer l'API avec la commande :
```
uvicorn main:app --reload
```

## Création des tables et insertion des données 
1. Ouvrir un nouveau terminal et se déplacer dans le dossier API :
```
cd API
```
2. Activer l'environnement virtuel Python :
```
.\venv\Scripts\activate
```
3. Exécuter le script de seed :
```
py seeder.py
```

## Démarrer l'application front React
1. Ouvrir un nouveau terminal et se rendre dans le dossier front
```
cd front
```
2. Installer les packages nécessaires
```
npm install
```
3. Lancer l'application React
```
npm start
```

# Documentation de l'API
## 📌 Introduction
Cette API permet de gérer une collection musicale comprenant des albums, morceaux, artistes et genres. Elle offre diverses fonctionnalités telles que :
- Récupération de la liste des albums et des détails d’un album spécifique.
- Récupération des morceaux d’un album et des morceaux d’un artiste.
- Gestion des genres musicaux.
- Inscription et connexion des utilisateurs avec authentification JWT.
- Ajout, modification et suppression d’albums, artistes et genres.

L’API est conçue pour faciliter la gestion d'une bibliothèque musicale et est intégrée à un front-end en React pour offrir une expérience utilisateur fluide.

## 📂 Structure des données
L'API repose sur une base de données contenant plusieurs entités :
- Album : contient un titre, une pochette (image), une date de sortie, une liste de morceaux et un artiste.
- Morceau : possède un titre, une durée, un artiste, un ou plusieurs genres et un album d'appartenance.
- Artiste : inclut un nom, un avatar (image) et une biographie.
- Genre : comprend un titre et une description.
- Utilisateur : contient un nom d’utilisateur, un mot de passe et une adresse email.

Un jeu de données initial est généré grâce à des seeders pour faciliter le développement et le test de l’API.

Base URL : http://localhost:8000

## 🏷️ 1. Exemple d'Endpoints de l'API
Cette documentation présente uniquement quelques endpoints à titre d'exemple. L'API complète contient d'autres fonctionnalités non décrites ici.

### 🔹 1.1. Récupérer la liste des albums
- URL : /api/albums/
- Méthode : GET
- Description : Retourne la liste de tous les albums enregistrés.
- Réponse attendue (200 OK) :
```
[
  {
    "id": 1,
    "title": "Album 1",
    "cover": "album1.jpg",
    "artist_id": 1,
    "release_date": "2020"
  },
  {
    "id": 2,
    "title": "Album 2",
    "cover": "album2.jpg",
    "artist_id": 2,
    "release_date": "2022"
  }
]
```

### 🔹 1.2. Récupérer un album par ID
- URL : /api/albums/:id
- Méthode : GET
- Description : Retourne un album spécifique selon son ID.
- Exemple de requête :
```
GET /api/albums/1
```

Réponse attendue (200 OK) :
```
{
  "title": "Abbey Road",
  "cover": "/assets/albums/abbey-road.jpg",
  "artist_id": 1,
  "release_date": "1969-09-26",
  "id": 1
}
```

### 🔹 1.3. Modifier un album par son ID

URL : /api/albums/:id
Méthode : PUT
Description : Modifie les informations d’un album spécifique.
Corps de la requête (JSON) :
```
{
  "title": "string",
  "cover": "string",
  "artist_id": 0,
  "release_date": "string"
}
```

Réponse attendue (200 OK) :
```
{
  "title": "string",
  "cover": "string",
  "artist_id": 2,
  "release_date": "string",
  "id": 1
}
```

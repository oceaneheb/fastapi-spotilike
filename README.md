# fastapi-spotilike

# Pré-requis 
Avant de lancer le projet, assurez-vous d'avoir installé les logiciels suivants sur votre ordinateur :
- Python
- Node.js

# Lancement de l'API
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
pip install fastapi uvicorn
```
4. Lancer l'API avec la commande :
```
uvicorn main:app --reload
```

# Création des tables et insertion des données 
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

# Démarrer l'application front React
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
npm run dev
```

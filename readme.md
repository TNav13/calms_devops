# Application Compteur Flask

Une application web full-stack simple avec compteur interactif, construite avec Flask, SQLite et Docker.

## 📋 Description

Cette application permet de gérer un compteur avec les fonctionnalités suivantes :
- **+1** : Incrémente le compteur de 1
- **+10** : Incrémente le compteur de 10
- **-1** : Décrémente le compteur de 1
- **-10** : Décrémente le compteur de 10
- **Reset** : Remet le compteur à 0

Toutes les modifications sont automatiquement sauvegardées dans une base de données SQLite persistante.

## 🚀 Technologies utilisées

- **Backend** : Flask (Python 3.12)
- **Frontend** : HTML5, CSS3, JavaScript (Vanilla)
- **Base de données** : SQLite
- **Conteneurisation** : Docker & Docker Compose

## 📁 Structure du projet

mon-projet/
├── app.py                  # Application Flask principale
├── requirements.txt        # Dépendances Python
├── Dockerfile             # Configuration Docker
├── docker-compose.yml     # Orchestration Docker
├── .dockerignore          # Fichiers exclus du build Docker
├── README.md              # Documentation
├── data/                  # Données persistantes
    └── counter.db         # Base de données SQLite
    └── templates/
    └── index.html         # Interface utilisateur


## 🛠️ Installation locale (sans Docker)

### Prérequis
- Python 3.12 ou supérieur
- pip

### Étapes

1. **Cloner le projet**
git clone 
cd mon-projet

2. **Créer un environnement virtuel**
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate


3. **Installer les dépendances**
pip install -r requirements.txt


4. **Lancer l'application**
python app.py


5. **Accéder à l'application**
Ouvrir le navigateur sur : `http://localhost:5000`

## 🐳 Installation avec Docker

### Prérequis
- Docker Desktop installé
- Docker Compose (inclus dans Docker Desktop)

### Méthode 1 : Docker Run

1. **Construire l'image**
docker build -t compteur-flask .

2. **Lancer le conteneur**
docker run -d -p 5000:5000 -v $(pwd)//app/data –name compteur compteur-flask


3. **Accéder à l'application**
Ouvrir le navigateur sur : `http://localhost:5000`

### Méthode 2 : Docker Compose (recommandée)

1. **Démarrer l'application**
docker-compose up -d


2. **Voir les logs**
docker-compose logs -f


3. **Arrêter l'application**
docker-compose down


## 📡 API Endpoints

L'application expose les endpoints suivants :

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Affiche la page principale |
| GET | `/api/get-counter` | Récupère la valeur actuelle |
| POST | `/api/increment` | Incrémente de 1 |
| POST | `/api/increment-ten` | Incrémente de 10 |
| POST | `/api/decrement` | Décrémente de 1 |
| POST | `/api/decrement-ten` | Décrémente de 10 |
| POST | `/api/reset` | Remet à 0 |

### Exemple d'utilisation de l'API

Obtenir la valeur actuelle
curl http://localhost:5000/api/get-counter

Incrémenter de 1
curl -X POST http://localhost:5000/api/increment

Reset
curl -X POST http://localhost:5000/api/reset


## 🔧 Configuration

### Variables d'environnement

- `FLASK_APP` : Nom du fichier principal (par défaut : `app.py`)
- `PYTHONUNBUFFERED` : Active les logs en temps réel (valeur : `1`)

### Port

Par défaut, l'application écoute sur le port **5000**. Pour changer le port :

**En local** : Modifier dans `app.py`
app.run(debug=True, host=‘0.0.0.0’, port=8080)


**Avec Docker** : Modifier le mapping de ports
docker run -p 8080:5000 compteur-flask


## 💾 Persistance des données

La base de données SQLite est stockée dans le dossier `data/counter.db`. 

Avec Docker, un volume est monté pour garantir la persistance des données même après l'arrêt du conteneur.

## 🧪 Tests

Pour tester manuellement l'application :

1. Ouvrir `http://localhost:5000`
2. Cliquer sur les différents boutons
3. Vérifier que le compteur se met à jour
4. Redémarrer l'application et vérifier que la valeur est conservée

## 🐛 Résolution de problèmes

### Le bouton ne s'affiche pas
- Vider le cache du navigateur : `Cmd+Shift+R` (Mac) ou `Ctrl+F5` (Windows/Linux)
- Vérifier que le fichier `index.html` est dans le dossier `templates/`

### Erreur "Module not found: flask"
pip install Flask


### L'application ne démarre pas avec Docker
Vérifier les logs
docker logs compteur
Reconstruire l’image
docker-compose up –build


### La base de données n'est pas persistée
- Vérifier que le volume est correctement monté
- S'assurer que le dossier `data/` existe

## 📝 Licence

Ce projet est sous licence MIT.

## 👤 Auteur

Développé dans le cadre d'un exercice DevOps.

## 🔗 Ressources

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation SQLite](https://www.sqlite.org/docs.html)

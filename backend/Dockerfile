# Utiliser une image Python officielle légère
FROM python:3.12-slim-bookworm

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . .

# Créer un répertoire pour la base de données SQLite
RUN mkdir -p /app/data

# Exposer le port 5000
EXPOSE 5000

# Variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Commande pour lancer l'application
CMD ["python", "app.py"]

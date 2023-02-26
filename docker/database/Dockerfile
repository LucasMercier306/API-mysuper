FROM postgres:latest

# Configuration de la base de données et de l'utilisateur
ENV POSTGRES_DB superdboscar
ENV POSTGRES_USER oscarsuperuser
ENV POSTGRES_PASSWORD Lzm$9ZLcQG55

# Exécution de la commande SQL pour créer la base de données
COPY create_db.sql /docker-entrypoint-initdb.d/

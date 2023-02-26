
# SUPER API #

## DEVELOPPEMENT ##

### GENERAL ###

- Ce projet utilise fastapi géré par le manager poetry.
- Pour lancer le projet: ```poetry run uvicorn main:api --reload```.
- Pour éditer le code durant le developpement il faut lancer l'environnement. Pour ajouter cet environnement à visual studio code, il faut faire ```poetry env info```, puis récuperer le path du binaire python puis le mettre en paramètre dans visual studio code. 

### POSTGRES INFO ###

- Le serveur postgres qui heberge la base de données est lancé via docker en mode developpement sur le port 5432 en localhost. On peut créer la base de données en faisant:

```
#On se place à la racine du projet

docker build -t superdboscar ./docker/database/.
docker run -d --name superdboscar-container -p 5432:5432 superdboscar

```
Voici les informations de connexion vers la base de données:

- **user:** oscarsuperuser
- **password:** rootpassword
- **urlPostGresServer:** localhost OU superdboscar-container au sein du réseau interne docker
- **portPostGresServer:** 5432
- **DB_NAME:** superdboscar

## PRODUCTION ##
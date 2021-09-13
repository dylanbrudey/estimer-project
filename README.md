# estimer-project

## Contexte
Projet Estimer dans lequel nous interrogeons une api (random-user-api) afin de récupérer les données publiques d'un utilisateur lambda et les afficher dans notre console.

## Projet

Installation à faire pour démarrer le projet

### Get the project

```
git clone https://github.com/dylanbrudey/estimer-project.git
```

### Project setup

#### Installation

##### Création d'un environnement virtuel

###### Windows
```
python -m venv ./api/venv
```
###### Unix
```
python3 -m venv ./api/venv
```
##### Lancement de l'environnement virtuel

###### Windows
```
.\api\venv\Scripts\activate
```
###### Unix
```
source api/venv/bin/activate
```
##### Installation des dépendances
###### Windows
```
pip install .\requirements.txt
```
###### Unix
```
pip3 install ./requirements.txt
```

#### Lancement du programme
###### Windows
```
python -m src\main.py
```
###### Unix
```
python3 -m src/main.py
```

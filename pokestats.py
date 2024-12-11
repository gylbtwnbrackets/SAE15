import markdown
import requests
import json
import os
import requests


#Statistiques calculée 
# Proportions de type par région :
# - On va dans l'url https://pokeapi.co/api/v2/pokemon/{id or name}/encounters dans location area puis dans 


# Fonctions à implémenter
def download(url: str, cache: str) -> dict: 
    """Télécharge les données JSON depuis une URL et les sauvegarde dans un fichier spécifique."""


    response = requests.get(url)
    json_data = response.json()

    # Écrit les données dans le fichier cache
    with open(cache, "w") as f:
        json.dump(json_data, f)

    return json_data  
## Get dataset : télécharge les données de la requête en JSON et les Convertis en Dictionnaire python 
def dataset()-> dict:
    link = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(link)
    json_data = response.json()
    return json_data

## Compute statistics : Calcule les statstiques 
#def compute_statistics() :

## Data set to MD  : Produit un Markdown à partir des données JSON de l'API 
#def dataset_to_md(dataset: dict, filename: str) -> None :
## Infos Locales 
#def infos_locales() -> None :
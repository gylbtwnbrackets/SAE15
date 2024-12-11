import markdown
import requests

# Fonction pour récupérer les données d'un Pokémon

def download_poke(id:int) :

    link = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(link)
    json_data = response.json()
    return json_data

# Fonction pour convertir un fichier Markdown en HTML
def md_to_html(fichier_markdown :str, fichier_html: str) -> None:

    with open (fichier_markdown, "r", encoding="UTF-8") as f :
        txt = f.read()

    html = markdown.markdown(txt)

    with open(fichier_html, "w", encoding="UTF-8") as g:
        g.write(html)

def pokefiche(id: int):
    data = download_poke(id)
    if not data:
        print(f"Aucun Pokémon trouvé pour l'ID {id}.")
        return

    # Récupérer les informations nécessaires
    sprite = data["sprites"]["front_default"]
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    types = data["types"]
    stats = data["stats"]

    str_type = ""
    if len(types) > 1:
        for i in range(len(types)):
            str_type += types[i]["type"]["name"] + " "
    else:
        str_type += types[0]["type"]["name"] + " "

    # Formatage des statistiques en Markdown
    stats_md = ""
    if len(stats) > 0:
        for stat in stats:
            stats_md += f"{stat['stat']['name']} : {stat['base_stat']}\n\n"

    # Contenu Markdown pour la page secondaire
    contenu_md_secondaire = f"""
{name}
========================================================

![Image de {name}]({sprite})

## Informations générales
- **Nom** : {name}
- **Taille** : {height} cm
- **Poids** : {weight} kg
- **Types** : {str_type}

## Statistiques
{stats_md}
"""
    

    # Sauvegarder le fichier Markdown pour la page secondaire
    fichier_markdown_secondaire = f"pokemon_{id}.md"
    with open(fichier_markdown_secondaire, "w", encoding="UTF-8") as f:
        f.write(contenu_md_secondaire)

    # Convertir en HTML pour la page secondaire
    fichier_html_secondaire = f"pokemon_{id}.html"
    md_to_html(fichier_markdown_secondaire, fichier_html_secondaire)
    print(f"Page secondaire pour {name} générée : {fichier_html_secondaire}")

    # Contenu Markdown pour la page principale
    contenu_md_principale = f"""
Pokémon 25
========================================================

<a href="pokemon_{id}.html">
<img src="{sprite}" alt="{name}" width="150" style="display:block; margin:10px auto;">
**{name}**
</a>
"""
    contenu_html_principale = f"""
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Location BMW</title>

    <link rel="stylesheet" type="text/css" href="styles.css" />

    <script src="https://kit.fontawesome.com/5f54a5c31c.js" crossorigin="anonymous"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Kode+Mono:wght@400..700&family=Orbitron:wght@400..900&display=swap"
        rel="stylesheet">

    <link
        href="https://fonts.googleapis.com/css2?family=Audiowide&family=Titillium+Web:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700&display=swap"
        rel="stylesheet">

    <link
        href="https://fonts.googleapis.com/css2?family=Audiowide&family=Rajdhani:wght@300;400;500;600;700&family=Titillium+Web:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700&display=swap"
        rel="stylesheet">
</head>
"""
    
    contenu_md_principale = contenu_html_principale + contenu_md_principale

    # Sauvegarder le fichier Markdown pour la page principale
    fichier_markdown_principale = "index.md"
    with open(fichier_markdown_principale, "w", encoding="UTF-8") as f:
        f.write(contenu_md_principale)

    # Convertir en HTML pour la page principale
    fichier_html_principale = "index.html"
    md_to_html(fichier_markdown_principale, fichier_html_principale)
    print(f"Page principale générée : {fichier_html_principale}")



import markdown
import requests

# Fonction pour récupérer les données d'un Pokémon
def download_poke(id: int):
    link = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(link)
    if response.status_code != 200:
        return None
    return response.json()


def get_translation(info: list, lang: str) -> str:
    for elt in info:
        if elt["language"]["name"] == lang:
            return elt["name"]
    return f"Traduction introuvable pour la langue : {lang}"

"""
info = [
    {"language": {"name": "en", "url": "https://pokeapi.co/api/v2/language/9/"}, "name": "Pikachu"},
    {"language": {"name": "fr", "url": "https://pokeapi.co/api/v2/language/5/"}, "name": "Pikachu"},
    {"language": {"name": "es", "url": "https://pokeapi.co/api/v2/language/7/"}, "name": "Pikachu"}
]
"""

def css():
    contenu_css = """

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-image: url("background.jpeg");
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: hidden;
}

.pokedex {
    background-color: #ff3b3b;
    border: 5px solid #000;
    border-radius: 15px;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);
    width: 400px; 
    height: auto; 
    position: relative;
    padding: 20px;
    overflow: hidden;
}

/* Top Circle */
.cercle {
    width: 50px;
    height: 50px;
    background-color: #bde0fe;
    border: 3px solid #fff;
    border-radius: 50%;
    position: absolute;
    top: 20px;
    left: 20px;
    box-shadow: 0 0 15px #00e7ff;
}

/* Small Lights */
.lumière {
    display: flex;
    gap: 10px;
    position: absolute;
    top: 25px;
    right: 20px;
}

.led {
    width: 15px;
    height: 15px;
    background-color: #00ff00;
    border-radius: 50%;
    border: 2px solid #fff;
}

.led.rouge {
    background-color: #ff0000;
}

.led.jaune {
    background-color: #ffff00;
}

.pokemon {
    background-image: url("background2.webp");
    background-size: cover;
    border: 4px solid #333;
    width: 90%;
    height: 200px;
    margin: 100px auto 20px;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.pokemon img {
    width: 200px;
    height: 200px;
}

.butons {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin: 10px 0;
}

.buton {
    width: 30px;
    height: 10px;
    border-radius: 5px;
}

.buton.jaune {
    background-color: #ffff00;
}

.buton.bleu {
    background-color: #0000ff;
}

.info {
    background-color: #8bc34a;
    border: 2px solid #333;
    border-radius: 10px;
    width: 90%;
    margin: 10px auto;
    padding: 15px; 
    text-align: left; 
    font-size: 16px; 
    color: #000;
    overflow-y: auto; 
    max-height: 300px; 
}

@media (max-height: 600px) {
    body {
        height: auto;
        overflow-y: auto;
        align-items: flex-start;
    }

    .pokedex {
        margin: 20px auto;
    }
}

    """
    
    # Sauvegarder le contenu CSS dans un fichier
    with open("styles.css", "w", encoding="UTF-8") as f:
        f.write(contenu_css)
    print("CSS créé : styles.css")

# Fonction pour convertir un texte Markdown en HTML
def md_to_html(content_md: str) -> str:
    return markdown.markdown(content_md)

# Fonction principale pour générer une fiche Pokémon
def pokefiche(id: int):
    css()
    data = download_poke(id)
    if not data:
        print(f"Aucun Pokémon trouvé pour l'ID {id}.")
        return

    # Récupérer les informations nécessaires
    sprite = data["sprites"]["front_default"]
    name = data["name"]
    height = data["height"] 
    weight = data["weight"] 
    stats = data["stats"]
    types = data["types"]

    species_url = data["species"]["url"]
    species_data = requests.get(species_url).json()
    translated_name = get_translation(species_data["names"], "fr")

    # Récupérer les types en français
    type_names = []
    for t in types:
        type_data = requests.get(t["type"]["url"]).json()
        translated_type = get_translation(type_data["names"], "fr")
        type_names.append(translated_type)
    str_type = ", ".join(type_names)

    stats_md = ""
    if len(stats) > 0:
        for stat in stats:
            stats_md += f"{stat['stat']['name']} : {stat['base_stat']}\n\n"

    contenu_md = f"""
## Informations générales
- **Nom** :  {translated_name}
- **Taille** : {height /10} m
- **Poids** : {weight /10} kg
- **Types** : {str_type}

## Statistiques
{stats_md}
"""

    # Convertir le Markdown en HTML
    contenu_html = md_to_html(contenu_md)

    # Structure HTML complète
    contenu_html_complet = f"""
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokédex - {name}</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="pokedex">
        <div class="cercle"></div>
        <div class="lumière">
            <div class="led rouge"></div>
            <div class="led jaune"></div>
            <div class="led"></div>
        </div>
        <div class="pokemon">
            <img src="{sprite}" alt="{name}">
        </div>
        <div class="info">
            {contenu_html}
        </div>
    </div>
</body>

</html>
    """

    # Sauvegarder dans un fichier HTML
    fichier_html = "index.html"
    with open(fichier_html, "w", encoding="UTF-8") as f:
        f.write(contenu_html_complet)

    print(f"Page principale générée : {fichier_html}")

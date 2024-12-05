import markdown
import requests 

def download_poke(id:int) :

    link = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(link)
    json_data = response.json()
    return json_data

def pokefiche(id : int) :
    with open("resultats.html", "w", encoding="UTF-8") as f:
        f.write("<h1> Résultats </h1>")
        link = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(link)
        json_data = response.json()
        #SPRITE
        sprite = json_data["sprites"]["front_default"]
        f.write('<img src="' + sprite + '")>')
        
        #NOM
        name = json_data["name"]
        f.write("<br>" +"name : "+ name+"</br>")
        #TAILLE 
        

        height =  json_data["height"]
        f.write("<br>"+"height : " + str(height)+"</br>")
        # POIDS
        weight = json_data["weight"]
        f.write("<br>"+"weight : " + str(weight)+"</br>")
        # TYPES
        types = json_data["types"]
        str_type = ""
        if len(types) > 1 :
            for i in range(len(types)):
                str_type += types[i]["type"]["name"] + " "
        else :
            str_type += types[0]["type"]["name"] + " "
        f.write("<br>"+"type : "+str_type +"</br>")


        # STATISTIQUES 
        stats = json_data["stats"]
        hp = stats[0]["stat"]["name"] +" : "+ str(stats[0]["base_stat"])
        attack = stats[1]["stat"]["name"] +" : "+ str(stats[1]["base_stat"])
        defense = stats[2]["stat"]["name"] +" : "+ str(stats[2]["base_stat"])
        special_attack = stats[3]["stat"]["name"] +" : "+ str(stats[3]["base_stat"])
        special_defense = stats[4]["stat"]["name"] +" : "+ str(stats[4]["base_stat"])
        speed = stats[5]["stat"]["name"] +" : "+ str(stats[5]["base_stat"])
        f.write("<br>"+hp+"</br>")
        f.write("<br>"+attack+"</br>")
        f.write("<br>"+defense+"</br>")
        f.write("<br>"+special_attack +"</br>")
        f.write("<br>"+special_defense +"</br>")
        f.write("<br>"+speed+"</br>")

        return sprite

def md_to_html(fichier_markdown :str, fichier_html: str) -> None:

    with open (fichier_markdown, "r", encoding="UTF-8") as f :
        txt = f.read()

    html = markdown.markdown(txt)

    with open(fichier_html, "w", encoding="UTF-8") as g:
        g.write(html)

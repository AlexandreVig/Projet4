import csv
import folium
# création de la carte zoom sur la France
m = folium.Map(location=[46.227638, 2.213749], zoom_start=5)


# fonction pour récupérer tout les centres de vaccination
def centrevaccination(fichier):
    tab = []  # on créé une nouvelle liste "tab"
    # on ouvre le fichier csv encodé en utf-8
    f = open(fichier, "r", encoding="utf-8")
    lignes_toutes = f.readlines()  # on récupère toutes les lignes
    # on enlève la première ligne pour ne pas prendre le nom des colonnes
    lignes_sans_premiere = lignes_toutes[1:]
    for ligne in lignes_sans_premiere:  # on parcours toutes les lignes sauf la première
        # on créé une liste "test" avec pour chaque élément une case de la ligne que l'on parcours
        test = ligne.split(";")
        # on ajoute la liste "test" a notre liste "tab" pour créé une une liste de liste
        tab.append(test)
    f.close()  # on ferme le fichier
    return tab  # on retourne la liste de liste


def addmarker(tabcentre):  # fonction pour ajouter les marker sur la carte
    for i in range(720):  # on répète 720 fois pour ajouter 720 marker c'est la limite de marker sur la carte qu'on a trouvé sinon le code ne fonctionne pas
        name = tabcentre[i][1] + "<br>" + \
            tabcentre[i][34] + "<div id='Localité'>" + \
            tabcentre[i][5] + \
            "</div>"  # on définit le message qu'il y aura écrit quand on clique sur les markers
        # on récupère la coordonnée gps de chaque centre que l'on met dans une liste pour séparer la latitude et la longitude
        loc = tabcentre[i][33].split(",")
        print(loc)
        folium.Marker(  # on créer le marker
            # on définit la localisation de chaque marker avec la liste "loc" qu'on a créé juste avant
            location=[loc[0], loc[1]],
            popup=name,  # on définit le message
            icon=folium.DivIcon(  # on  définit l'icon du marker où l'on écrit le nom, la ville, l'adresse, le site internet et le numéro de téléphone de chaque centre pour les récupéré plus tard
                html=f"""<img src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/images/marker-icon.png" style="margin-left: -12px; margin-top: -41px; width: 25px; height: 41px;"><div class="localite" style="display: none;">{tabcentre[i][5]}</div><div class="site" style="display: none;">{tabcentre[i][24]}</div><div class="tel" style="display: none;">{tabcentre[i][25]}</div><div class="nom" style="display: none;">{tabcentre[i][1]}</div><div class="adresse" style="display: none;">{tabcentre[i][34]}</div>""")
        ).add_to(m)  # on ajoute le marker sur la carte


# appelle de la fonction "centrevaccination"
tabcentre = centrevaccination("covid19-france-lieu-vaccination.csv")
addmarker(tabcentre)  # appelle de la fonction "addmarker"
m.save("index.html")  # on sauvergarde la carte dans le fichier "index.html"

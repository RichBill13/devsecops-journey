import json
import requests
import sys

# securite: verifier qu'un nom d'artiste a bien ete transmis dans le terminal
if len(sys.argv) != 2:
    sys.exit()

# envoi de la requete sur internet(l'appel API)
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# convertir la reponse en dictionnaire python
o = response.json()

# parcourir les resultats et afficher uniquement le titre des chansons
for result in o["results"]:
    print(result["trackName"])
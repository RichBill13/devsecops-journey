## bibliotheque/library
-c'est un fragment de code ecrit par moi ou par d'autre, que nous pouvons utiliser dans nos programmes
-python permet de partager des fonctions ou des fonctionnalites avec d'autres sous forme de <modules>

-<une bibliotheque>: est un ensemble structuree de plusieurs modules, elle offre une solution globale pour resoudre un probleme complexe ou realiser un domaine d'application. c'est generalement un dossier composer de plusieurs fichier (.py) interconnectes(on parle aussi de <package>)

-<un module>: est une seule unite de code(generalement un seul fichier) creee pour accomplir un ensemble de taches precises. c'est simplement un fichier(.py)

## module random
c'est un module qui contient plusieurs fonction.
concretement le module <random> c'est le tiroir marque <evenements aleatoires>, il contient plusieurs fonctions differentes:
-<choice()>: qui est un outil precis range dans ce tiroir(qui sert a tirer un element au sort dans une liste. ex: <coin = choice (["heads", "tails"])>)
-<randint()>: qui sert a tirer un nombre(ex: <number = random.randint(1, 10)>)
-<shuffle()>: qui sert a melanger une liste
-etc

## differente maniere d'importer des modules
-<import random>: juste cette ligne de code permet d'importer l'integralite du contenus des fonctions de <random>
-<from random import choice>: par contre celle ci permet d'etre plus precis sur ce que nous souhaitons importer en l'occurence la fonction <choice>

## module statistics
a l'interieur se trouve plusieurs fonction mais celle que nous allons voir est <mean>
-<mean>: est une fonction qui prend une liste de valeurs et affiche la moyenne de ces valeurs.


## Arguments de la ligne de commande
ici, au lieu de fournir toutes les valeurs au sein du programme que nous avons cree, nous voulons plutot pouvoir recevoir des entrees depuis la ligne de commande. ex: au lieu de <python average.py> mais plutot <python average.py 100 90>

## module Sys
est un module qui nous permet de prendre des arguments en ligne de commande

## Argv
est une liste au sein du module <sys> qui enregistre ce que  l'utilisateur a saisi sur la ligne de commande
-<sys.argv[1]>: c'est ou l'argument entree par le user sera stocke.
-<sys.argv[0]>: c'est ou le nom du programme sera stocke.
- il faut utiliser un <try   except> pour des erreurs du style le user n'a pas entre d'argument: <list index out of range>
- pour plus de securite et etre sur de prendre en compte tout les cas d'erreurs( pas d'arguments, trop d'argument, argument exact), on doit utiliser un <if  else> avec la fonction <len>.
ex: <if len(sys.argv) < 2:>
- actuellement notre code est logiquement correct, cependant il est tres avantageux de separer la gestion des erreurs du reste du code(voir fichier <name.py> pour la version finale et correcte)

## Technique slicing
le slicing(ou decoupage) est une technique qui permet d'extraire une partie d'une sequence(une liste, une chaine de caractere, un tuple) en specifiant les indices de debut et de fin.
-<sequence[start : stop : step]>: les 3 parametres represente
-<start>: l'indice de depart(inclus). par defaut cet indice est <0>
-<stop>: l'indice de fin(exclus). par defaut c'est la fin de sequence
-<step>: le pas/l'intervalle de saut. par defaut <1>
-on peut utiliser les <slice> sur des chaines de caracteres, une liste, une liste d'arguments.

## Cowsay
-<definition technique>: c'est une application CLI(command line argument) ecrit en PERL qui prend une chaine de caracteres en entree(via l'entree standard ou un argument) et la formate dans une bulle de dialogue ASCII a cote d'un dessin d'animal compose de caracteres texte.
-<definition simple>: c'est un logiciel bien connu qui permet a une vache de parler a un utilisateur
-<installation avec python>: on utilise le gestionnaire de paquet <pip> pour installer, cependant , vu la protection classique introduite par le systeme <norme PEP 668> sur Ubuntu/Debian/Linux, pour eviter que <pip> n'ecrase les fichiers systeme et ne casse notre OS, Linux bloque desormais l'installation globale de paquets avec <pip>.
Voici les 2 solutions:
-1<utiliser un environnement virtuel(venv)>(recommande): c'est la methode la plus propre et la norme en developpement Pyton. elle isole nos paquets <pip> dans un dossier dedie.
-<sudo apt update && sudo apt install python3-venv python3-full -y>: commande pour installer le paquet systeme <python3-venv>
-<python3 -m venv .venv>: commande pour creer un environnement virtuel dans notre projet
-<source .venv/bin/activate>: commande pour activer l'environnement virtuel(on le fait a chaque nouvel ouverture de terminal)
-<pip install cowsay
    python3 name.py>: commande pour installer <cowsay> et pour lancer le script contenu dans notre fichier <name.py>
-<deactivate>: commande qui permet de sortir de l'environnement virtuel

-2<forcer l'installation globale>: si nous sommes deja sur une machine virtuelle de labo/test et que nous voulons installer le paquet rapidement sans creer d'environnement virtuel.
-<python3 -m pip install cowsay --break-system-packages>, puis on execute normalement le script (python name.py)

## API<application programming interface/interface de programmation d'application>
Ils permettent de se connecter au code d'autres personnes.

## requests
c'est un module qui permet a votre programme de se comporter comme un navigateur web. Elle permet d'envoyer des requettes HTTP et de recevoir la reponse du serveur directement dans le code.
Pour une meilleur comprehension du module <requests> voir le fichier 
[Ouvrir mon fichier](../weekly-reviews/python-reviews/itunes.py)

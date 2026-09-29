## bibliotheque/library
-c'est un fragment de code ecrit par moi ou par d'autre, que nous pouvons utiliser dans nos programmes
-python permet de partager des fonctions ou des fonctionnalites avec d'autres sous forme de <modules>

-<une bibliotheque>: est un ensemble structuree de plusieurs modules, elle offre une solution globale pour resoudre un probleme complexe ou realiser un domaine d'application. c'est generalement un dossier composer de plusieurs fichier (.py) interconnectes(on parle aussi de <package>)

-<un module>: est une seule unite de code(generalement un seul fichier) creee pour accomplir un ensemble de taches precises. c'est simplement un fichier(.py)

## random
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


## Arguments de la ligen de commande
ici, au lieu de fournir toutes les valeurs au sein du programme que nous avons cree, nous voulons plutot pouvoir recevoir des entrees depuis la ligne de commande. ex: au lieu de <python average.py> mais plutot <python average.py 100 90>

## Sys
est un module qui nous permet de prendre des arguments en ligne de commande

## Argv
est une liste au sein du module <sys> qui enregistre ce que  l'utilisateur a saisi sur la ligne de commande
-<sys.argv[1]>: c'est ou l'argument entree par le user sera stocke.
-<sys.argv[0]>: c'est ou le nom du programme sera stocke.
- il faut utiliser un <try   except> pour des erreurs du style le user n'a pas entre d'argument: <list index out of range>
- pour plus de securite et etre sur de prendre en compte tout les cas d'erreurs( pas d'arguments, trop d'argument, argument exact), on doit utiliser un <if  else> avec la fonction <len>.
ex: <if len(sys.argv) < 2:>
- actuellement notre code est logiquement correct, cependant il est tres avantageux de separer la gestion des erreurs du reste du code(voir fichier <name.py> pour la version finale et correcte)
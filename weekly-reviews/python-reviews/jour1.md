-la commande pour executer un fichier nomme <hello.py> dans le terminal est : <python hello.py>
-l'ordinateur ne comprends que des 0 et des 1
par consequent lorsqu'on execute <python hello.py>,
python interprete le texte et le converti en 0 et 1 
comprehensible par l'ordianteur.
- une chaine de caractere appelee <string> en python on note <str> est une sequence de texte
-les fonctions prennent des arguments qui influencent leur comportement
-la fonction <print> insere automatiquement un saut de ligne lors de son execution. cependant nous pouvons fournir un argument <end> en notre faveur pour que la creation d'une nouvelle ligne ne soit pas effectuee!
-la maniere la plus elegante d'utiliser des chaine de caractere
# name = input ("what's your name? ")
# print(f"hello, {name}")
-le <f>, il s'agit d'un indicateur special permettant a python de traiter cette chaine de caracteres d'une maniere particuliere

## la methode strip
permet de supprimer les espaces avant ou apres une saisie
ex: <name = input("what's your name? ")
name = name.strip()
print(f"hello, {name}")>

## la methode title
permet de mettre la premiere lettre de mot  saisi en majuscules
ex: <name = name.title()>

fichier: hello.py

## la conversion de type
c'est une operation qui consiste a changer temporairement le type d'une variable en une autre

## la lisibilite l'emporte
quelle que soit la methode de programmation choisie, n'oubliez pas que votre code doit etre lisible. Utilisez des commentaires pour vous expliquer, ainsi qu'aux autres, le fonctionnement de votre code.

## la methode round()
permet d'arrondir un chiffre a l'entier le plus proche

## utilisation de round() pour formater l'affichage des grand nombre
-<print(f"{z:,}")>

## declaration de fonction
-<def hello(to):
    print("hello", to)
    >
NB: <python est un langage indente>
-<to>: sert a faire signifier que notre fonction prend un seul parametre.
-nous ne sommes pas obliger de placer notre fonction au debut de notre programme. On peut la deplacer plus bas, mais il faut alors indiquer a l'interpreteur qu'il s'agit d'une <main> fonction et d'une autre <hello> fonction distincte.
-surtout ne pas oublier d'appeler la <main> fonction si non rien ne va se passer.
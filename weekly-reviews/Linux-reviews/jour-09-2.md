## SHELL SCRIPTING
pour automatiser un ensemble de commandes, vous devrez apprendre a ecrire des scripts shell. ces scripts sont concus pour etre executes par l'interpreteur de commandes <bash>.
ex: saisir <find -name "*.c" -ls> dans la ligne de commande revient a executer un fichier script contenant les lignes suivantes:
-<#!/bin/bash>
-<find . -name "*.c" -ls>
La premiere ligne du script, qui commence par <#!>, contient le chemin complet de l'interpreteur de commandes(ici c'est /bin/bash) a utiliser sur le fichier. mais il faut garder a l'esprit qu'il ya plusieur interpreteur de commandes  autre que <bash> tels que <python>,<perl>,<csh> etc. et dans ces cas la le chemin complet de l'interpreteur devra etre modifie: </usr/bin/python>...

## Valeur de retour
Tous les scripts shell generent une valeur de retour a la fin de leur execution, qui peut etre explicitement definie avec l'option <exit>

## Affichage des valeurs de retour
Lors de l'execution d'un script, il est possible de verifier une valeur ou une condition specifique et de renvoyer un resultat indiquant la reussite ou l'echec.Par convention, la reussite est renvoyee par (0), et l'echec par toute valeur non nulle.
ex: <ls /etc/logrotate.conf>
<etc/logrotate.conf>
<$ echo $?>
<0>
Dans cet exemple, le systeme parvient a localise le fichier </etc/logrotate.conf> et la commande <ls> renvoie la valeur 0 pour indiquer la reussite de l'operation. si elle est executee sur un fichier enexistant, elle renvoie <2>

## Syntaxe de base et caracteres speciaux
les scripts exigent le respect d'une syntaxe standard.
-<#>: utilise pour ajouter un commentaire
-<\>: utilise a la fin d'une ligne pour indiquer la poursuite sur la ligne suivante
-<;>: utilise pour interpreter ce qui suit comme une nouvelle commande a executer apres l'execution de la commande en cours. grace a elle , plusieurs commande peuvent etre place sur la meme ligne.
-<$>: indique ce qui suit est une variable d'env
-< > >: sortie de redirection; ecrire une sortie dans un fichier 
->>: Ajouter la sortie
-<: redirection de l'entree
-<|> utilise pour rediriger le resultat vers la commande suivante
-<\>: utiliser pour fractionner les commandes lorsqu'elles sont tres longue
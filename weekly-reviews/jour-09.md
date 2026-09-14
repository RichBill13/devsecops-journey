## Rappel des commandes precedentes
<Bash> concerve l'historique des commandes saisies. pour afficher la liste des commandes executees, saisissez simplement <history> dans la ligne de commande.

## recherche et utilisation des commandes precedentes
<haut/bas>: parcourez la liste des commandes precedemment executees
<!!>(prononce bang-bang): execute la commande precedente
<Ctrl + R>: recherche les commandes precedemment utilisees

## File Permission/Propriete du fichier
Sous linux et d'autres systemes d'explotation de type UNIX, chaque fichier est associe a un user qui en est le proprietaire. chaque fichier est egalement associe a un groupe qui a un interet pour ce fichier et certains droits, ou permissions.
-<chown>: utilise pour modifier le proprietaire d'un fichier ou d'un repertoire
-<chgrp>: utilise pour modifier la propriete du groupe
-<chmod>: Permet de modifier les permissions du fichier, ce qui peut se faire separement pour le proprietaire, le groupe et le reste du monde.

## Modes d'autorisation des fichiers et chmod
les fichiers possedent trois types de permissions:
-<r>: lecture
-<w>: ecriture
-<x>: execution
elles sont generalement representees sous la forme <rwx>. Ces permissions concernent trois groupes de proprietaires:
-<u>: l'utilisateur/proprietaire
-<g>: le groupe
-<o>: les autres
par consequent, on dispose des trois groupes de trois autorisations suivants:
rwx: rwx: rwx
  u:  g:   o
## ls -l somefile
commande pour liste le fichier <somefile> avec ses proprietes
## chmod uo+x,gw somefile
commande pour attribuer au proprietaire et aux users la permission d'execution, et supprimer la permission d'ecriture pour le grouupe

ce type de syntaxe peut etre difficile a saisir et a memoriser, on utilise donc une notation abregee permettant de definir toutes les permissions en une seule etape
-4: lecture
-2: ecriture
-1: execution
ainsi, 
-7: lecture/ecriture/execution
-6: lecture/ecriture
-5: lecture/execution

## outils en ligne de commande pour la manipulatiion de fichiers texte

## cat
elle sert a lire et a afficher des fichiers, ainsi qu'a simplement visualiser leur contenu, pour afficher un fichier

## tac fichier1 fichier2 > fichier3
concatene le contenu de fichier1 avec celui de fichier2 et enregistre le resultat dans un nouveau fichier

## cat > <nomdufichier>
cette commande cree un nouveau fichier et attend que le user saisisse le texte.

## echo
affiche simplement du text

## les fichiers volumineux

## less somefile et cat somefile | less
ces deux commandes permettent de consulter un fichier.

## head
cette commande lit les premieres lignes de chaque fichier specifie(10 par defaut) et les affiche sur la sortie standard. le nombre <10> peut etre modifier dans une option.
ex: imprimer les 5 premieres lignes du fichier /etc/default/grub
<head -n 5 /etc/default/grub> ou encore <head -5 /etc/default/grub>

## Tail
cette command affiche les dernieres ligens de chaque fichier specifie sur la sortie standard. par defaut elle affiche les 10 dernieres lignes.
<tail -n 15 somefile.log> ou <tail -15 somefile.log>

## Affichage des fichiers compresses
lorsqu'on travaille avec des fichiers compresses, de nombreuses commandes standard ne sont pas direntement utilisables. il existe une version de commande speciale concue specialement pur fonctionner sur les fichiers compresses. ils sont generalement precedes de la lettre <z>
-<zcat fichier-compresse.txt.gz>: pour visualiser un fichier compresse
-<zless somefile.gz> ou <zmore somefile.gz>: pour parcourir un fichier compresse
-<zgrep -i less somefile.gz>: pour effectuer une recherche a l'interieur d'un fichier compresse
-<zdiff fichier1.txt.gz fichier2.txt.gz>: comparer deux fichiers compresses

## Introduction a sed et awk
sont des commandes permettant de modifeir, et d'extraire le contenu des fichiers

## sed (stream editor)
un outil puissant de traitement de texte, il permet de  modifier le contenu d'un fichier ou d'un flux d'entree, generalement en le placant dans un nouveau fichier ou flux de sortie.
cette commande permet de filtrer le texte et d'effectuer des substitutions dans les flux de donnees.
-<sed -e commande> <nom_de_fichier>: specifiez les commandes d'edition sur la ligne de commande, traitez les donnees d'entree d'un fichier et affichez la sortie sur la sortie standard(par exemple le terminal)
-<sed -f scriptfile> <nom_de_fichier>: specifiez un fichier script contenant des commandes <sed>, effectuez les operations sur ce fichier et affichez la sortie sur la sortie standard
-<echo " je te hais " | sed s/haine/amour/>: utilisez <sed>pour filtrer l'entree standard et placer la sortie sur la sortie standard.

## awk
cette commande permet d'extraire puis d'afficher des elts specifiques d'un fichier et est souvent utilisee pour generer des rapports.
-<fichier de commande awk>: specifiez une commande directement sur la ligne de commande
-<awk -f fichier de script>: specifiez un fichier contenant un script a executer.

## File manipulation

## sort
cette commande permet de reorganiser les lignes d'un fichier texte, par ordre croissant ou decroissant, selon une cle de tri.( -t permet de trier selon un champ specifique du fichier.)
-<sort nomdufichier>: trie les lignes du fichier specifie, selon les caracteres au debut de chaque ligne
-<cat fichier1 fichier2 | sort>: Fusionnez les deux fichiers, puis triez les lignes et affichez le resultat sur le terminal
-<sort -r nomdufichier>: trier les lines dans l'ordre inverse
-<sort -k 3 nomdufichier>: tier les lignes en fonction du troisieme champ de chaque ligne plutot que du debut.

## uniq
supprime les lignes consecutives dupliquees dans un fichier texte et est utile pour simplifier l'affichage du texte
-<sort fichier1 fichier2 | uniq > fichier3> ou <sort -u fichier1 fichier2 > fichier3 > : pour supprimer simultanement les entrees en double de plusieurs fichiers.
-<uniq -c nomdefichier>: pour compter le nombre d'entrees en double.

## paste fichier1 fichier2
pour coller le contenu de deux fichiers

## paste -d ' ' fichier1 fichier2
tout en utilisant un delimiteur

## join
est une version ameliorer de la fonction <paste>
-<join fichier1 fichier2>

## split
est une commande qui permet de diviser un fichier en segment de taille egale pour faciliter leur consultation et leur manipulation
-<split linux.words lwords>:

## grep
est un outil de recherche de texte principal. il analyse les fichiers a la recherche de motifs specifiques et peut etre utilise avec des expressions regulieres.
-<grep [modele] nomfichier>: recherche un motif dans un fichier et imprime toute les lignes correspondantes
-<grep -v [modele] nomfichier>: imprime toute les lignes qui ne correspondent pas au motif
-<grep [0-9] nomfichier>: imprime les lignes contenant les nombres de 0 a 9
-<grep -C 3 [modele] nomfichier>: affiche le contexte des lignes pour la correspondance avec le motif

## strings
elle permet d'extraire toute les chaines de caracteres imprimable presentes dans le ou les fichiers fournis en arguments. elle est utile pour localiser du contenu lisible par l'humain integre dans des fichiers binaires, pour les fichiers texte, on peut simplemt utiliser <grep>
-<strings book1.xls | grep my_string>: recherche la chaine de caractere <my_string> dans une feuille de calcul.

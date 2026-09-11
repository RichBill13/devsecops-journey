# Lab 01 — recherche repertoire et creation de liens symbolique

## Objectif

utiliser find pour rechercher un repertoire et ensuite utiliser ln pour creer un lien symbolic

## Commandes exécutées

## /tmp> find / -type d -name init.d
mais cette commande va sorti beaucoup de permission denied donc il y'a 2 alternatives, soit on utilise sudo , soit (stderr) pour rediriger les erreurs a dev/null

## /tmp> sudo find / -type d -name init.d
## /tmp> fing / -type d -name init.d 2> /dev/null

## cd ~
on retourne dans notre home avant de creer le lien symbolique.

## ln -s /etc/init.d
creation du lien symbolique

## ls -l init.d
commande pour confirmer que le lien a bien ete creer( le (l) au debut de la ligne et le (->) indiquent que init.d est un lien symbolique)

## definition 
-Un lien symbolique, est l'equivalent sur linux d'un raccourci sous windows. c'est un fichier special, il pointe simplement vers le chemin d'un autre fichier ou repertoire.
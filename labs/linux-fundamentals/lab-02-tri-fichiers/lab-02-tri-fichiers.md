# Lab 04 — Trier les fichiers par date de modification

## Objectif

Créer plusieurs fichiers et identifier le fichier le plus récemment modifié depuis le terminal.

## Commandes executees

## echo "premiere version du journal de l'application" > application.log
{
    -echo: produit du texte;
    -(>): ecrit ce texte dans un fichier/ou remplace si il ya deja un texte dans le fichier;
}

## cat application.log
verification du contenu du fichier

## sleep 2
## echo "Premiere alerte de securite" > security.log
## sleep2
## echo "Premier evenement systeme" > system.log
creation de 2 autres fichiers et a chaque fois on sleep de 2 seconde pour avoir une difference de temps

## ls
on affiche les fichiers crees

## ls -lt
on trie par date de modification et le fichier le plus recent apparait en premier.
{
    -l: affiche les details
    -t: trie selon la date de modification
}

## ls -lt --time-style=long-iso
pour afficher les dates plus clairement.

## sleep 2
## echo "Nouvelle ligne ajoutee dans l'application" >> application.log
{
    -(>): remplace le contenu;
    -(>>): ajoute du contenu a la fin sans supprimer l'existant.
}

## cat application.log
on verifie a nouveau le contenu

## ls -lt
on trie a nouveau les elements par date.

## stat application.log
on examine precisement les donnees du fichier application.log
{
    -stat: affiche plusieurs info notamment:
        *Access: le dernier acces au fichier;
        *Modify: la derniere modification du contenu;
        *Change: la derniere modification des metadonnees;
}

## ls -ltr
affiche le fichier le plus ancient en premier
{
    -(r): renverse l'ordre du classement.
}

## ls -1t | head -n 1
affiche uniquement le fichier le plus recent
{
    -ls -1t: affiche un nom par ligne et par modification;
    -head -n 1: conserve uniquement la premiere ligne;
}
![capture4](images/image4.png)
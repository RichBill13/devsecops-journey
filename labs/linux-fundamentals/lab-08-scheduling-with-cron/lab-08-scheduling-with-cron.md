# Lab 06 — programmer une tache periodique avec <cron>

## Objectif

programmer une tache qui execute une tache simple tout les jours at 10.

## Commandes exécutées

## sudo systemctl enable --now cron

## systemctl status cron

## nano /tmp/myjob.sh

## a l'interieur on mets
#!/bin/bash
echo Hello I am running $0 at $(date)

## chmod +x /tmp/myjob.sh
on rend le fichier myjob.sh en executable

## echo "5 11 * * */tmp/myjob.sh >> /tmp/myjob.log 2>&1
(chaque jour a 11h05, execute le script /tmp/myjob.sh, puis ajoute tout ce qu'il affiche ainsi que ses erreurs a la fin du fichier /tmp/myjob.log)
{
    -<0 10 * * *>: a la minute 5 de la 11eme heure, chaque jour de chaque mois
    -</tmp/myjob.sh>: lance le programme situe dans /tmp/myjob.sh
    -<>> /tmp/myjob.log>: prend l'affichage normal du script et ajoute-le a la suite du fichier myjob.log. le (>>) c'est pour dire : sans effacer ce qui s'y trouvait deja.
    -<2>&1>: redirige egalement tous les messages d'erreur au meme endroit que l'affichage normal.
}

## crontab mycrontab
sert a charger et enregistrer les instructions ecrites dans le fichier texte mycrontab

## crontab -l
permet de verifier que le fichier a bien ete chargee

## crontab -r
supprime la planification active completement, elle efface toutes les taches cron planifiees.
## lab 01 Apache wev server status/ gestion d'apache avec systemctl

## objectif
utilisation de systemctl pour monitorer et controler l'etat du server apache (gestion des services)

## Environnement

- Système : Ubuntu WSL2
- Utilisateur principal : `rich`
- Utilisateur créé : `linuxlab`
- Service etudie : `apache`

## Commandes exécutées

## systemctl status apache2 --no-pager
verification du status de apache2(active/inactive)
-no-pager(commande pour afficher directement le resultat dans le terminal).

## sudo systemctl start apache2
commande pour demarrer les services

## systemctl is-active apache2/curl -I http://localhost
commande pour verification du demarrage

## sudo systemctl stop apache2
commande pour arret du service apache

## systemctl is-active apache2
verification finale

![image3](images/image.png)
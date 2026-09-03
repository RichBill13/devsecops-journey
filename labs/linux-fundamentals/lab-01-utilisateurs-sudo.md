# Lab 01 — Utilisateurs et sudo

## Objectif

Créer un utilisateur, lui attribuer un mot de passe, lui donner accès à sudo et vérifier ses privilèges.

## Environnement

- Système : Ubuntu WSL2
- Utilisateur principal : `rich`
- Utilisateur créé : `linuxlab`

## Commandes exécutées


## whoami
 pour verifier avec quel utilisateur je suis entrain de travailler.

## sudo useradd -m -s /bin/bash linuxlab
pour creer le nouvel utilisateur linuxlab
{
    -sudo: execute la commande avec les privileges admin
    -useradd: commande qui cree le user
    -(-m): commande qui permet de creer un dossier personnel /home/linuxlab
    -(-s /bin/bash): configure bash comme shell
    -linuxlab: nom du nouvel utilisateur
}
## sudo passwd linuxlab
commande pour definir le mot de passe de l'utilisateur linuxlab

## sudo usermod -aG sudo linuxlab
commande pour autoriser l'utilisateur a utiliser SUDO
{
    -usermod: modifie un utilisateur existant
    -(-G sudo): ajoute l'utilisateur au groupe SUDO
    -(-a): conserve ses autres groupes et ajoute le nouveau // il est tres important, sans lui il pourra avoir remplacement des autres groupes de l'utilisateur.
}
## groups linuxlab
pour verifier les differents groupes de l'utilisateur

## su - linuxlab
commande qui permet de passer sur le nouveau compte/changer d'utilisateur.

## whoami
## pwd
pour verifier son dossier

## ls /root
commande pour consulter le dossier personnel de root// nb: on teste sans SUDO pour confirmer que cela est impossible car un utilisateur ordinaire ne peut pas consulter le dossier personnel de root

## sudo ls -la /root
commande pour consulter le dossier personnel de root

## sudo whoami
## exit
pour sortir du compte linuxlab

## Suppression de l’utilisateur de test

### Objectif

Supprimer l’utilisateur `linuxlab` ainsi que son dossier personnel afin de pouvoir recommencer le lab depuis le début.

## exit
pour quitter la session linuxlab

## id linuxlab
verifier l'existance de l'utilisateur que l'on souhaite supprimer// la commande id affiche les information concernant un user(sont UID(identifiant utilisateur), GID(son groupe principal), ses groupes supplementaire)

## ls -ld /home/linuxlab
{
    -ls: affiche les informations sur un fichier ou un dossier
    -(-l): utilise un affichage detaille
    -(-d): affiche les informations du dossier lui meme au lieu d'afficher son contenu
    -/home/linuxlab est le dossier personnel de l'utilisateur
}
cette verification permet de confirmer  le dossier qui sera supprime.

## sudo userdel -r linuxlab
{
    -sudo: execute la commande avec les privileges root
    -userdel: supprime un compte utilisateur
    -(-r): supprime egalement son dossier personnel et ses fichiers associes.
    -linuxlab: l'utilisateur cible
}
sans l'option (-r), le compte serait supprime, mais le dossier /home/linuxlab pourrait rester present.
cette commande est destructive: le contenu de /home/linuxlab est supprime. il faut donc toujours verifier le nom de l'utilisateur avant de l'executer.

## id linuxlab
pour verifier que l'utilisateur a bien ete supprime// id: ‘linuxlab’: no such user

## ls -ld /home/linuxlab
verifier que son dossier a ete supprime// ls: cannot access '/home/linuxlab': No such file or directory


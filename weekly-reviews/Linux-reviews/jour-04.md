## Essential CLI skills

## Ctrl + Alt + T
Commande pour ouvrir le terminal sur Ubuntu

## Cat
affiche le contenu d'un fichier/combine ou concatene plusieurs fichiers

## head
affiche les premieres ligne d'un fichier

## tail
affiche les dernieres lignes d'un fichier

## man
ouvre la page de commande d'un document

## the pipe symbol (|)
son role est de prendre le resultat d'une commande et de l'utiliser comme entree dans une autre commande.

## Quelques definitions
-Une commande: c'est un programme specifique, ou un script auquel on demande au terminal de l'executer
-Une Option:  sont des commutateurs, generalement precedes d'un seul tiret (-) pour des formes courtes ou d'un double tiret(--) pour des formes longues, qui modifient ou developpent le comportement d'une commande.
-Un Argument: precise la cible d'une commande en  definissant le fichier, le chemin d'acces ou les donnees exacts que la commande doit traiter.

## sudo (switch user and do)
permet a un utilisateur d'executer des commandes avec les privileges d'un autre utilisateur( en general "root"), sans toute fois se connecter comme cet utilisateur directement.

## su and type the password
C'est la commande pour devenir root

## sudo visudo -f /etc/sudoers.d/username (remplacer username par le nom de l'utilisateur)
commande pour donner l'acces sudo a un autre compte

## chmod 440 /etc/sudoers.d/username
pour attribuer les permissions si neccessaire.

## definitions
A virtual terminal: is a full screen text-session that runs entirely outside the graphical environment.
-to switch to one VT for another: Ctrl+Alt+F3(F3 is VT3)

## sudo systemctl isolate multi-user.target
commande pour switch du system au mode text-only

## sudo systemctl isolate graphical.target
commande pour ramener l'interface graphique

## sudo systemctl stop gdm && sudo systemctl start gdm
commande pour demarrer ou arreter le display manager service

## ssh nom_user@adresse_du_serveur(example: ssh student@remote-server.com ou ssh student@192.168.1.50)
SSH est le protocole standard sous linux pour prendre la main a distance sur une autre machine de facon securisee(chiffree).

## shutdown -h(use sudo)
pour arreter le systeme(eteindre), h(halt)

## shutdown -r(use sudo)
pour reboot le system

## which diff
ou se trouve le programme que le systeme va lancer si je tape diff

## whereis diff
ou se trouve le programme diff, ses sources et sa documentation sur le systeme

## type diff
type c'est une commande qui indique la nature reelle d'une commande, un programme sur disque, un alias ou une foncton

## (/) absolute pathname begin with it, the root directory
## (../../) relative pathname

## cat
utiliser pour regarder a l'interieur des petits fichiers; on ne peut pas scroll

## tac
utiliser pour regarder des fichier en commencant par la derniere ligne.

## less
utiliser pour regarder des fichiers assez large et permet le scroll, permet aussi de rechercher et de naviguer a l'interieur du fichier.

## touch
utiliser pour creer des fichiers et modifier leurs timestamp

## rmdir sampdir
permet de supprimer le repertoire sampdir si et seulement si il ya rien a l'interieur

## rm -rf sampdir
permet de supprimer le repertoire et les sous repertoires

## stdin, stdout, stderr
les 3 differents 
{
    -(<): permet de lire les donnees depuis le fichier au lieu du clavier
    -(>): ecrase le fichier s'il existe et y ecrit le resultat normal
    -(2>): les messages d'erreur sont enregistres dans le fichier, la sortie normale reste a l'ecran.
    -(>>): ajouter du contenu sans ecraser
}

## definition
A PIPE takes the output of one command and feeds it directly in as the input of the next. (|)

## structure a 2 niveaux pour les package management(package managment system)
Linux divise la gestion des logiciels en deux categories

##  1. Outils de bas niveau(dpkg, rpm)
-travaille sur les fichiers de paquets locaux(.deb ou .rpm)
-ils installent ou desinstallent un fichier precis, mais ne savent pas telecharger sur internet et ne gere pas les dependances.

##  2. Outils de haut niveau(apt, dnf, zypper)
-se connectent aux depots distants sur internet
-resolvent automatiquement les dependances(si le paquet A a besoin du paquet B, ils telechargent et installent A et B ensemble.)
-utilisent les outils de bas niveau en arriere plan pour faire le travail d'extraction.

## Famille Debian/Ubuntu (apt) : (dnf)Famille Red Hat/Fedora
-apt update
-apt search foo(chercher un paquet)
-apt install foo(installer un paquet)
-apt remove foo(supprimer un paquet)
-apt autoremove(nettoyer les dependances inutiles)
-apt upgrade(mettre a jour tout le systeme)

## apt update
ne met a jour aucun logiciel. il telecharge uniquement la liste actualisee des paquets disponibles sur les serveurs.

## apt upgrade
telecharge et installe les nouvelles versions des logiciels a partir de cette liste.

## apt remove
supprime le programme mais garde ses fichiers de configuration

## apt purge
supprime le programme et ses fichiers de configuration.
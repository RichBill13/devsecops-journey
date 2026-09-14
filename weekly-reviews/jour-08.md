## Apercu des editeurs sous Linux

A un moment ou a un autre le besoin de modification manuelle des fichiers texte se fera sentir. les sys admin Linux sont souvent tenter de priviligier les utilitaires graphiques pour creer et modifier les fichiers de config system, cependant, cette methode peut s'averer moins performante.
En effet les logiciels de traitement de texte ne sont pas de simples editeurs de texte, ils ajoutent de nombreuses informations de mise en forme supplementaires(generalement invisible) qui risque de rendre le fichier de config systeme inutilisables.

## methode de creation de fichier sans editeur

## echo
-echo ligne 1 > myfile
-echo ligne 2 >> myfile
-echo ligne 3 >> myfile

## cat
-cat <<EOF> monfichier
->ligne une
->ligne deux
->ligne trois
->EOF

## Methode de creation de fichier avec editeur de texte

## nano
-<nano <nom_du_fichier>>/si le fichier n'existe pas, il sera creer
{
    -<Ctrl + G>: Afficher l'ecran d'aide
    -<Ctrl + O>: Ecrire dans un fichier
    -<Ctrl + X>: Quitter un fichier
    -<Ctrl + R>: Inserer le contenu d'un autre fichier dans la memoire tampon actuelle.
    -<Ctrl + C>: Afficher la position du curseur
}

## gedit
c'est un editeur graphique simple d'utilisation, fonctionnant exclusivement dans un environnement graphiquee
-<gedit <nom_du_fichier>>

## code visual studio
c'est un editeur graphique simple d'utilisation.

## introduction a VI(VIM)
le programme installe sur mon systeme est generalement <vim> et egalement connu sous le nom de <vi>. c'est un outils standard , installe sur la casi totalite des distributions Linux.
Lors de l'utilisation de <vim>, toutes les commandes sont saisis au clavier. il n'est pas necessaire de deplacer constamment les mains pour utiliser un peripherique de pointage comme une souris ou un pave tactile, sauf si je souhaite le faire dans l'une des versions graphiques de l'editeur.

## Modes dans vim
<vim> propose trois mode, 
-<le mode commande>: par defaut , <vim> demmarre en mode commande. chaque touche correspond a une commande de l'editeur(les frappes au clavier sont interpretees comme des commandes permettant de modifier le contenu des fichiers)
-<le mode inserer>: Tapez <i> pour passer du mode commande au mode insertion.ce mode permet d'inserer du texte dans un fichier. appuyez sur <echap> pour quitter le mode insertion et revnir au mode commande.
-<le mode Doubler>:Tapez <:> pour passer du mode commande au mode ligne. chaque touche correspond a une commande externe, permettant par example d'ecrire le contenu d'un fichier sur le disque ou de quitter.

## Travaillez avec les fichiers dans vim
-<vim mon fichier>: Lance l'editeur et modifiez <mon fichier>
-<vim -r monfichier>: demarrer et modifier <monfichier> en mode de recuperation apres un plantage systeme
-<:r fichier2>: Lire le fichier2 et inserer a la position actuelle
-<:w>: ecrire dans le fichier
-<:w monfichier>: ecrire dans <monfichier>
-<:w! fichier2>: ecraser le <fichier2>
-<:x ou :wq>: quitter et enregistrer le fichier modifie
-<:q> quittee
-<:q!>: quitter meme si les modifications n'ont pas ete enregistrees.

## modification de la position du curseur dans vim
-<j> ou <ret>: pour descendre d'une ligne
-<k>: pour avancer d'une ligne vers le haut
-<h>: pour deplacer un caractere vers la gauche
-<l>: pour deplacer un caractere vers la droite
-<0>: pour aller au debut de la ligne
-<$>: pour se deplacer en fin de file
-<w>: pour passer au debut du mot suivant
-<:0> ou <1G>: pour  aller su debut du fichier
-<:n> ou <nG>: pour passer a la ligne n
-<:$> ou <G>: pour passer a la derniere ligne du fichier
-<Ctrl + F> ou <Page suivante>: pour avancer d'une page
-<Ctrl + B> ou <page precedente>: pour revenir en arriere d'une page
-<^l>: pour actualiser et centrer l'ecran.

## recherche de texte dan vim
-</modele>: recherchez le modele
-<?modele>: recherchez le motif a rebours

## touche utilisees pour rechercher du texte dans vim
-<n>: passer a l'occurence suivante du modele de recherche
-<N>: passer a l'occurence precedente du modele de recherch

## travaillez avec du texte dans vim
<un>: Ajouter du texte après le curseur ; s'arrêter à la touche Échap .
<UN>: Ajouter du texte à la fin de la ligne courante ; s'arrêter à la touche Échap
<je>: Insérer le texte avant le curseur ; arrêter à la touche Échap . ...
<je>: Insérer le texte au début de la ligne courante ; arrêter à la touche Échap
<o>:	Commencez une nouvelle ligne sous la ligne actuelle, insérez-y le texte ; arrêtez-vous à la touche Échap .
<O>:	Commencez une nouvelle ligne au-dessus de la ligne actuelle, insérez-y le texte ; arrêtez-vous à la touche Échap .
<r>:	Remplacer le caractère à sa position actuelle.
<R>:	Remplacer le texte à partir de la position actuelle ; s'arrêter à la touche Échap .
<x>:	Supprimer le caractère à la position actuelle
<Nx>:	Supprimer N caractères, à partir de la position actuelle
<dw>	Supprimez le mot à sa position actuelle.
<D>:	Supprimez le reste de la ligne actuelle
<dd>:	Supprimer la ligne actuelle
<Ndd ou dNd>	Supprimer N lignes
vous	Annuler l'opération précédente
<yy>	Copiez la ligne actuelle et placez-la dans le tampon.
<Nyy> ou yNy	Copiez N lignes et placez-les dans le tampon.
<p>	Collez à la position actuelle la ou les lignes extraites du tampon.

## utilisation de commande externes dans vim
la commande <sh> ouvre une invite de commandes externe. lorsque je quitte cette invite, je reprend ma session d'edition.

## Environnement Utilisateur

## comptes, utilisateurs et groupe

## whoami
commande qui permet d'identifier l'utisateur actuel
-<whoami -a>: permettra d'obtenir des informations plus detaille

## qui
commande pour afficher la liste des users actuellement connectes

## ordre des fichiers de demarrage
lors de ma premiere connexion a linux, la procedure standard consiste a lire et a evaluer le fichier </etc/profile>, puis a rechercher les fichiers suivants(s'ils existent) dans l'ordre indique:
-<~/.bash_profile>
-<~/.bash_login>
-<~/.profile>
le repertoire personnel de l'utilisateur est designe par <~/>.
a chaque ouverture d'une nouvelle fenetre de terminal, on n'execute pas une nouvelle connexion systeme complete.

## Creation d'alias
on peut creer des commandes personnalisees, ou modifier le comportement de commandes existantes en creant des <alias>. ces <alias> sont places dans le fichier <~/.bashrc> afin d'etre dispo pour tous les interpreteurs de commandes que l'on cree.
la commande <unalias> supprime un alias.

## Principe de base des utilisateurs et des groupes

chaque user Linux se voit attribuer un identifiant utilisateur unique <uid> qui est simplement un entier
les users normaux commencent avec un <uid> de <1000> ou plus.

Linux utilise les <groupes> pour organiser les users. les <groupes> sont des ensembles de comptes partageant certaines permissions; ils permettent de constituer un ensemble d'utilisateurs ayant des interets commun en matiere de droits d'acces, de privileges de securite.

la gestion des groups s'effectue via le fichier </etc/group>, qui repertorie les groupes et leurs membres.
les users possedent un ou plusieurs identifiant de groupe <gid>

## Ajout er suppression des users

## sudo useradd bjmoose
cette commande par defaut, definit le repertoire personnel sur </home/bjmoose>, le remplit de quelques fichiers de base et ajoute une ligne a </etc/passwd>

## sudo userdel bjmoose
supprime le compte user <bjmoose>, cependant le repertoire <home/bjmoose> restera intact.
pour supprimer avec le repertoire, il faut ajouter <-r>

## id
permet d'obtenir des infos sur le user actuel

## ajout et suppression des groupes
## sudo /usr/sbin/groupadd nomdugroupe
pour ajouter un groupe
## sudo /usr/sbin/groupdel nomdugroupe
pour delete le groupe
## sudo /usr/sbin/usermod -a -G nomdugroupe nomdugroupe
pour ajouter un user a un groupe

## le compte racine
le compte <root> possede des pouvoirs tres etendus et un acces complet au systeme.
on peut toutefois utiliser <sudo> pour attribuer des privileges plus limites aux comptes de users

## su et sudo
lors de l'attribution des privileges, la commande <su> permet de lancer une nouvelle session shell sous un autre nom d'utilisateur.
NB: l'utilisation de <su> pour l'attribution des privileges est presque toujours une mauvaise pratique, cela peut entrainer la suppression de fichiers systeme vitaux et des failles de securite.

l'octroi des privileges via <sudo> est moins risque et preferable.

## elevation au compte racine
Pour devenir temporairement superutilisateur pour une serie de commandes, taper <su> et le systeme va nous demander ensuite le mdp root.

pour executer une seule commande avec les privileges root, tapez <sudo><commande>, une fois la commande terminee, vous redeviendrez un user normal sans privileges.

les fichiers de config de <sudo> sont stockes dans le fichier </etc/sudoers> et dans le repertoire </etc/sudoers.d/>.

## variables environnementales
se sont des quantites qui possedent des valeurs specifiques et qui peuvent etre utilisees par l'interpreteur de commandes, comme <bash>.

## definition des variables d'environnement
-afficher la valeur d'une variable specifique <echo $SHELL>
-exporter une nouvelle valeur de variable <exporter VARIABLE=valeur> ou <VARIABLE=valeur; exporter VARIABLE>
-Ajouter une variable de facon permanente: modifier <~/.bashrc> et ajouter la ligne <export VARIABLE=valeur>.

## la variable HOME
il represente le repertoire personnel ou de connexion de l'utilisateur. la commande <cd> permet d'y acceder.
-<echo $HOME /home/student> et <cd /bin>: Afficher la valeur de la variable d'env <HOME>, puis changer de repertoire(cd) ver </bin>

## la variable PATH
le <PATH> est une liste ordonnee de repertoires(chemin d'acces) qui est analysee lors de l'execution d'une commande afin de trouver le programme ou le script approprie.
chaque repertoire est separe par deux-points(:)
<echo PATH=$HOME/bin:$PATH>

## la variable SHELL
la variable d'env <SHELL> pointe vers l'interpreteur de commandes par defaut du user(le programme qui gere tout ce que vous tapez dans une fenetre de commande, generalement bash
)
<echo $SHELL /bin/bash>
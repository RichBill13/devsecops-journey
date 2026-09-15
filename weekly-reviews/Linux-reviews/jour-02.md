## partitions and filesystem

when navigating the linux environment, it is essential to distinguish between the physical storage(the hardware) and the logical organization(the software).

sans systeme de fichier, une partition n'est qu'un ensemble brut de 0 et 1. En formatant une partition, vous installez un systeme de fichiers specifique, tel que ext4 ou XFS.

Le montage est un processus qui fait le lien entre la partition et votre structure de dossier accessible. sous linux, on n'utilise pas les lettres comme C ou D:. a la place , on rattache le systeme de fichiers d'une partition a un repertoire specifique, appele point de montage.

## comparaison des concepts de stockage entre windows et linux

Disk 1         /dev/sda1  : identification de partition
NTFS/VFAT      ext4/ XFS/ Btrfs: type de system de fichier
Drive Letter(E,D)  Mount Point: parametre de montage
C:\             /:Base du fichier(root/admin), ou le OS est stocke


Sous Windows, chaque partition ou lecteur est considéré comme une entité distincte identifiée par une lettre. À l'inverse, Linux intègre toutes les partitions dans une arborescence unique et unifiée. Cela signifie qu'au lieu de basculer vers un « lecteur D », il suffit de naviguer vers un dossier spécifique (le point de montage) où le système de fichiers de cette partition a été monté.


## Filesystem Hierarchy Standard
c'est une specification qui definit les noms, les emplacements et les fonctions prevues des repertoires sur les systemes Linux.

## key FHS top-level Directories

-(/: root) = la racine du systeme de fichier entier, tous les fichiers et dossier y vivent.
-(/home) = le  repertoire personnel de tout utilisateur
-(/root) = le repertoirer principal, aucun autre user n'y a acces.
-(/etc) = tous les fichiers de configurations y sont.
-(/bin & /usr/bin) = la boite a outil de tout les jours
-(/sbin & /usr/sbin) = la boite a outils pour les commandes d'administration systeme.
-(/var) = le journal de bord et les registres(les fichiers logs qui changent constamment).
-(/tmp) = la poubelle temporaire (fichiers effaces au redemarrage).
-(/dev) = device files. Linus represente le materiel(cle usb, disque dur, terminal) comme un fichier dans ce repertoire(/dev).
-(/proc) = le tableau de bord en temps reel sur la memoire, le processeur et les processus en cours.
-(/run/media/utilisateur) = l'entree pour les peripheriques amovibles.

## Case Sensitivity
Linux traite les majuscules et les miniscules  dans les noms de fichiers et de repertoire de maniere distincte.
ce qui veut dire , que nous devons etre exact lorsqu'on ecris les chemins d'acces des fichiers
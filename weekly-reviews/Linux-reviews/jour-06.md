## the ps Command
ps(process status) affiche les informations a propos des processus en cours d'execution sur le systeme.

## ps -u <username>
affiche les processus appartenant a un utilisateur specifique

## ps -ef 
affiche chaque processus sur le systeme avec tout les details

## ps -eLf

## pstree
affiche les precessus hierachises sous forme d'un arbre

## the top command
affiche les donnees du systeme en continu, a la difference de ps qui affiche une fois, top affiche les donnees qui se mettent a jours continuellement jusqu'a ce que on appui sur la touche <q> pour quitter.

## scheduling a task

## Running a One-Off Task: at
permet d'executer une tache non interactive une fois, a une heure specifique.
<at 10:00 AM Jul 15>
at> /usr/local/bin/backup.sh
at> <EOT> # press Ctrl + D(pour sauvegarder) to finish
<atq>: pour lister les jobs en attente
<atrm>: pour annuler un job

## Running Recurring Tasks: cron
pour des taches qui ont besoin de se repeter sur un emploi de temps(par example, chaque nuit, chaque lundi etc).
<* * * * * /usr/local/bin/script.sh>: cette commande va s'executer chaque minute de chaque heure, chaque jour.
<30 08 10 06 * /home/sysadmin/full-backup>: cette commnade va s'executer a 8:30 a.m le 10 juin, peu importe le jour de la semaine.

## When the Machine isn't Always On: anacron
pour que les commandes <cron> fonctionnent , il faut que lorsque la tache veut s'executer, que la machine soit allumer, si il est eteint, la commande ne va pas s'executer et sera oublier.
<anacron> resous ce probleme, ce n'est pas un remplacant a <cron>, mais un compagnon, il est concu pour les taches qui ont besoin de s'executer periodiquement( jour, semaine, mois). si un agenda est rate a cause de la machine eteint, <anacron> recupere la tache et l'execute. son fichier de config est sous </etc/anacrontab>

## Pausing a Task: sleep
parfois, une commande doit attendre au lieu de s'executer a une heure fixe.
<sleep> suspend une execution pour le temps que nous specifions et apres reprend

## FILE OPERATIONS/FILE SYSTEM
Sous linux, le systeme de fichier  est structure comme un arbre et commence par le repertoire racine qui marque le debut de l'aborescence hierachique et est parfois designe par le terme <tronc> et est simplement note </>

## Varietes de systeme de fichiers
-ext3
-ext4
-courges
-btrfs

## partitions Linux
Dans la plupart des cas, chaque systeme de fichiers d'un systeme Linux occupe une partition de disque.
<les partitions> : permettent d'organiser le contenu des disques en fonction du type et de l'utilisation des donnees.
{
    -<racine(/)>: ou sont stockees les programmes essentiels au fonctionnement du systeme
    -<home(/home)>: ou sont stockees les fichiers des utilisateurs.
}

## Points de montage
Avant de pouvoir utiliser un systeme de fichier, on doit le monter sur l'arborescence des systemes de fichiers a un point de montage.
NB: si un systeme de fichiers est monte sur un repertoire non vide, son contenu sera ecraser et inaccessible tant que le systeme de fichiers n'est pas demonte. c'est pourquoi les points de montage sont generalement vide.

## Montage et Demontage

## mount
commande qui permet d'attacher un systeme de fichier(local ou reseau) a un point de l'arborescence du systemede fichiers.
ex: <sudo mount /dev/sda5 /home>: cette commande attachera le systeme de fichiers contenu dans la partition du disque associe au noeud peripherique /dev/sda5 a l'aborescence des systemes de fichiers au point de montage /home.

## umount
ex: <sudo umount /home>: pour demonter la partition

pour que le systeme de fichier soit disponible automatiquement au demarrage, vous devez modifier le fichier <etc/fstab>(fstab: file system table).
ce fichier affiche la config de tout les systemes de fichiers preconfigures.

## mount
l'execution de la commande mount sans argument affichera tous les systemes de fichiers actuellement montes.

## df -Th
affichera les infos sur les systemes de fichiers montes, notamment le type de systemede fichiers et les statisques d'utilisation de l'espace actuellement utilise et disponible.

## systemes de fichiers reseau et NFS
un systeme de donnees reseau peut stocker toutes ses donnees sur une seule machine ou les repartir sur plusieurs noeuds du reseau.

le systeme de fichier le plus utilise est simplement appele NFS(Network File system)

## les repertoires personnels des users distants sont places sur un SERVEUR et ils y ont acces depuis plusieur ordinateurs client

##

## NFS sur le serveur

## sudo systemctl start nfs
permet de demarrer les services nfs sur serveur
chaque fichier sous Linux possede trois permissions possible: <lecture>(r), <ecriture>(w), et <execution>(x).

le fichier texte </etc/exports> contient les repertoires et les permissions qu'un hote est pret a partager avec d'autres systeme via NFS.

apres toute modification dans ce fichier  il faut redemarrer les services <sudo systemctl restart nfs>. 

et si on veut un redemarrage automatique, <sudo systemctl enable nfs>

## NFS sur le client
sur la machine client, si on souhaite que le systeme de fichiers distant soit monte automatiquement au demarrage du systeme, le fichier </etc/fstab> est modifie a cet effet.
ex: <nom_serveur:/projects /mnt/nfs/projects nfs defaults 0 0>

## Apercu des repertoires personnel des users
ici je vais apprendre a differencier et a identifier les repertoires les plus importants sous linux.

## home
chaque user possede un repertoire </home>. et le repertoire </root> est le repertoire personnel du user root(admin).

## /bin et /sbin
le repertoire </bin> contient des fichiers binaires executables, des commandes essentielles utilisees pour demarrer le systeme ou en mode mono-utilisateur, et des commandes essentielles requises par tous les users du systeme, telles que <cat, cp, ls, mv, ps et rm>

le repertoire </sbin> est destine aux binaires essentiels lies a l'administration systeme, tel que <fsck et ip>.
<ls /bin /sbin>: permet d'afficher la liste

les commandes non essentielles au demarrage ou au fonctionnement du systeme em mode mono-utilisateur sont placees dans les repertoires </usr/bin> et </usr/sbin>.

## /proc
ils contiennent des fichies virtuels (fichier existant uniquement en memoire) permettant de visualiser les donnees du noyau, qui evoluent constamment. il ne contient pas des fichies physique, mais des informations systeme en cours d'execution

## /dev
il contient des noeuds peripherique, un type de pseudo-fichier utilise par la plupart des peripheriques materiels et logiciels, a l'exception des peripheriques reseau.
ce repertoire est :
-Vide sur la partition du disque lorsqu'elle n'est pas montee
-Contient des entrees creees par le systeme <udev>, qui cree et gere les noeuds de peripheriques sous linux.

## /var
il contient des fichiers dont la taille et le contenu sont susceptibles de changer pendant l'execution du systeme:
-les fichiers journaux</var/log>
-paquets et fichiers de base de donnees</var/lib>
-fichier d'impression</var/spool>
-fichier temporaires</var/tmp>

le repertoire </var> peut etre place sur son propre systeme de fichier afin de pouvoir gerer la croissance des fichiers et d'eviter que des augmentations soudaines de leur taille n'affectent gravement le systeme.
les repertoires services reseau tels que </var/ftp>(le service FTP) et </var/www>(le service web HTTP) se trouvent egalement sous </var>

## /etc
il contient des fichiers de config systeme que seul l'admin peut modifier. il ne contient aucun programme binaire, mais quelque scripts executables.
-</etc/resolv.conf>: indique au systeme ou trouver sur le reseau les correspondances entre noms d'hotes et adresse IP(DNS)
-des fichiers tels que <passwd>, <shadow> et <group>: permettent la gestion des comptes user et se trouvent sous </etc>

## /boot
il contient les quelques fichiers essentiels necessaires au demarrage du systeme.
pour chaque noyau installe sur le system, il existe 4 fichiers:
-<vmlinuz>: le noyau linux compresse, necessaire au demarrage
-<initramfs>: le systeme de fichiers RAM initial, necessaire au demarrage, parfois appele <initrd>
-<config>: le fichier de config du noyau, utilise uniquement a des fins de debogage et de gestion des donnees.
-<system.map>: table symboles du noyau, utilisee uniquement pour le debogage.

## /lib et /lib64
</lib> contient des bibliotheques pour les programmes essentiels situes dans /bin et /sbin.
le nom de ces fichiers bibliotheque commence par <ld> ou par <lib>

## /media, /run, /mnt
la plupart des systemes linux sont configures pour que tout support amovible soit automatiquement monte des qu'il est connecte.
ces points de montage sont places dans le repertoire </run>
ex: une cle USB nommee bill appartenant a un user kam sera montee a l'emplacement: </run/media/kam/bill>

le repertoire </mnt> est utilise pour le montage temporaire des systemes de fichiers

## repertoires supplementaire sous (/:)
-</opter>: logiciel d'application optionnels
-</sys>: systeme de fichier virtuel
-</srv>: donnees specifiques au site fournies par le systeme
-</tmp>: fichiers temporaire
-</utilisateur>: app multi-users

## l'arborescence du repertoire /usr
comporte des sous repertoires suivant:
-</usr/include>: fichiers d'en-tete pour compiler les app
-</usr/lib>: bibliotheque pour les programmes situes dans /usr/bin et /usr/sbin
-</usr/lib64>:bibliotheque 64 bits pour les programmes 64bits situes dans /usr/bin et /usr/sbin
-</usr/sbin>: fichiers binaire systeme non essentiels, tels que les demons systeme et les scripts
-</usr/partage>: donnees partagees utilisees par les app, generalement independantes de l'architecture
-</usr/src>: code source, generalement pour le noyau linux
-</usr/local>:donnees de programmes specifiques a la machine locale

## comparaison des fichiers avec diff
la commande diff permet de comparer les fichiers et des repertoires
<diff [options] <nom_fichier1> <nom_fichier2>> pour comparer 2 fichiers.

## Utilisation de l'utilitaie de fichiers
sous Linux, l'extension d'un fichier ne permet pas, par defaut, de determiner sa nature comme c'est le cas dans d'autre system. 
il faut utiliser l'utilitaie de fichier <file *>
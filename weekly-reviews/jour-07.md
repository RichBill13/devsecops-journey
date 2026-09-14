## Sauvegarde et Compression des donnees

il existe plusieurs facons de sauvegarder des donnees, en utilisant soit cp(la simple copie), ou l'utilisation de la commande la plus robuste <rsync>

-<rsync> est plus efficace car il verifie l'existence du fichier a copier. si le fichier existe et sa taille  et sa date de modification sont inchangees, il evite une copie inutile et gagne du temps.
tres efficace pour la copie recursive


-<cp> ne peut copier des fichiers que depuis et vers des destinations sur la machine locale(sauf si je copie depuis ou vers un systeme de fichiers monte via NFS)

## rsync -r project-X archive-machine:archives/project-X
NB: veuillez a specifier correctement les options et les chemins d'acces.
- toujours tester <rsync> avec l'option <-dry-run> afin de s'assurer qu'elle produit les resultats escomptes.

## Compression des donnees
les donnees des fichiers sont souvent compressees afin d'economiser de l'espace disque et de reduire le temps de transmission des fichiers sur les reseaux.
-<gzip>: l'utilitaire de compression Linux le plus frequemment utilise
-<bzip2>: genere les fichiers nettement plus petis que ceux produits par <gzip>
-<xz>:l'utilitaire de compression le plus econome en espace utilise sous Linux

## l'utilitaire tar
est souvent utilise pour regrouper des fichiers dans une archive puis compresser l'archive entiere en une seule fois.

## gzip
il compresse efficacement et tres rapidement
-<gzip *> compresse tout les fichiers du repertoire courant; chaque fichier est compresse et renomme avec l'extension .gz
-<gzip -r projetX>: compresse tous les fichiers du repertoire projetX, ainsi que tous les fichiers de tous les repertoires situes sous projetX
-<gunzip foo>: decompresse le fichier foo.gz .
en interne, la commande <gunzip> est en fait identique  a gzip -d

## bzip2
tres utiliser pour compresser les fichiers volumineux
-<bzip2>: compresse tous les fichiers du repertoire et remplace chaque fichier par un fichier renomme avec l'extension .bz2
-<bunzip2 *.bz2>: decompresse tous les fichiers ayant l'extension .bz2 dans le repertoire courant.
## bzip2 est obsolete

## xz
tres utiliser pour la compression des fichiers volumineux susceptibles d'etre telecharges depuis internet
-<xz *>: compresse tous les fichiers du repertoire courant et remplace chaque fichier par un fichier ayant l'extension .xz
-<xz foo>: compresse foo dans foo.xz en utilisant le niveau de compression par defaut(-6), et supprime foo si la compression reussit
-<xz -dk bar .xz>: decompresse bar.xz en bar et ne supprime pas bar.xz meme si la decompression reussit.
-<xz -dcf a.txt b.txt.xz > abcd.txt>: decompresse un melange de fichiers compresses et non compresses vers la sortie standard, a l'aide d'une seule commande.
-<xz -d * .xz>: decompresse les fichiers compresses a l'aide de xz.

## Gestion des fichiers zip
utiliser lorsque on recoit un fichier zip d'un user ou d'un environnement windows, ou encore apres un telechargement sur internet.
-<sauvegarde zip *>: compresse tous les fichiers du repertoire courant et les place dans le fichier backup.zip
-<zip -r backup.zip>: archivez votre repertoire de connexion(-) et tous les fichiers et repertoires qui s'y trouvent dans backup.zip
-<decompresser backup.zip>: extrait tous les fichiers contenus dans backup.zip et les place dans le repertoire courant.

## archivage et compression de donnees a l'aide d'un tar
il est possible de compresser les donnees lors de la creation de l'archive et de les decompresser lors de l'extraction de son contenu
-<tar xvf monredir.tar>: extrayez tous les fichiers contenus dans mydir.tar dans le repertoire mydir
-<tar zcvf monrepertoire.tar.gz monrepertoire>: creez l'archive et compressez-la avec gzip
-<tar jcvf monrepertoire.tar.bz2 monrepertoire>: creez l'archive et compressez-la avec bz2
-<tar jcvf mydir.tar.xz mydir>: creez l'archive et compressez-la avec xz
-<tar xvf monrepertoire.tar.gz>: extrayez tous les fichiers de mydir.tar.gz dans le repertoire mydir

on peut separer les etapes d'archivage et de  compression
<tar cvf mon rep.tar mon rep>; <gzip mon rep.tar>
mais cette methode est plus lente et gaspille de l'espace en creant un fichier <.tar> intermediaire inutile.

## copie de disque a disque (dd)
le programme <dd> est tres utile pour effectuer des copies de l'espace disque brut.
ex: <dd if=/dev/sda of=/dev/sdb>
NB: la copie d'un disque sur un autre effacera tout ce qui existait auparavant sur le second disque.

## tar = regrouper
il prend des dizaines ou des milliers de fichiers et dossiers separes et les colle ensemble pour en faire un seul gros fichier. cependant il ne reduit pas la taille des donnees

## gzip, bzip2, xz = compresser
ils sont responsable de la reduction de la taille des donnees

## on les utilise ensemble

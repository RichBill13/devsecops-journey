# Lab 06 —utilisation de diff et patch

## Objectif

Linux et d'autres communautés open source utilisent souvent l' utilitaire patch pour diffuser les modifications et les mises à jour. Nous proposons ici une introduction pratique à l'utilisation de diff et patch .

Il serait judicieux de consulter les pages de manuel de patch et diff pour en apprendre davantage sur les options et techniques avancées, ce qui permettra d'utiliser patch plus efficacement . En particulier, la forme des correctifs a une incidence importante sur leur acceptation.

Accédez au répertoire /tmp .
Copiez un fichier texte dans  /tmp . Par exemple, copiez /etc/group dans /tmp .
Utilisez l' utilitaire dd pour copier le fichier texte dans un nouveau fichier situé dans /tmp , en convertissant les caractères en majuscules : ` student:/tmp> dd if=/tmp/group of=/tmp/GROUP conv=ucase .` (Nous aborderons la commande dd plus loin). L' option `conv=ucase` convertit tous les caractères en majuscules. Si vous préférez, vous pouvez utiliser toute autre méthode pour modifier le fichier texte ; l'utilisation de dd n'est pas obligatoire .
D'après la page de manuel de la commande `patch` , l'option `-Naur` est recommandée pour préparer un patch avec `diff` lors de la comparaison récursive de deux arborescences de répertoires. Nous ignorerons l' option `-a` , qui consiste à traiter tous les fichiers comme du texte, car `patch` et `diff` ne doivent de toute façon être utilisés que sur des fichiers texte. Comme nous comparons simplement deux fichiers, il est inutile d'utiliser les options `N` ou `r` de `diff` , mais cela ne changera rien. Comparez `group` et `GROUP` à l'aide de `diff` , puis préparez un fichier de patch approprié.
Utilisez la commande patch pour modifier le fichier d'origine, /tmp/group , afin que son contenu corresponde à celui du fichier modifié, /tmp/GROUP . Vous pouvez essayer d'abord avec l' option --dry-run !
Enfin, pour vérifier que votre fichier original a bien été modifié et contient désormais uniquement des majuscules, utilisez la commande diff sur les deux fichiers. Les fichiers devraient être identiques et la commande diff ne devrait afficher aucun résultat .

## Commandes exécutées

## cd tmp

## cp /etc/group /tmp/group

## dd if=/tmp/group of=/tmp/GROUP conv=ucase
cette commande cree une version entierement en majuscule nommee GROUP

## diff -u group GROUP > group.patch
cette commande compare le fichier original <group> avec le fichier modifie <GROUP> et ensuite enregistre le resultat dans un fichier <group.patch>.
l'utilisation de <-u> (Unified format) est le format standard recommande pour creer des patchs lisibles

## patch --dry-run /tmp/group /tmp/group.patch
cette commande permet de simuler l'application du patch sur le fichier original et ainsi detecter les erreurs avant l'application du patch en lui meme.

## patch /tmp/group /tmp/group.patch
cette commande permet de modifier le fichier d'origine avec le patch genere

## diff /tmp/group /tmp/GROUP
verifie que les fichiers /tmp/group et /tmp/GROUP sont desormais strictement identiques.
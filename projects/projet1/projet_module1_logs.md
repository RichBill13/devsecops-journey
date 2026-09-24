## 1.1 Chasse aux données dans des logs
**Ce que tu fais**
- Génère un faux fichier de log d'accès web de 5 000 lignes (IP, date, méthode, URL, statut) avec un petit script.
- Réponds à 10 questions **uniquement en ligne de commande** : top 5 des IP, nombre de 404, requêtes par heure, URL les plus demandées, etc. (`grep`/`rg`, `awk`, `sed`, `sort`, `uniq -c`, `cut`, `head`, `tail`).
- Ajoute 5 questions sur le système de fichiers : les 10 plus gros fichiers de `/var`, ceux modifiés depuis 24 h (`find`, `du`).
- Écris `cheatsheet.md` : 25 commandes avec un exemple chacune.
- **Garde ce log**, tu le réutiliseras au projet 3.1.

**Outils gratuits :** Ubuntu sous WSL2, coreutils, ripgrep.
**Validé si :** tu refais chaque one-liner sans notes et tu expliques chaque étape du `|`.

## SOLUTION

## touch generate_log.py
creation du fichier qui va contenier notre script python de generation de logs

## python3 generate_log.py
cette commande permet d'executer le script python de generation de logs

## identifier le top 5 des ip
## partons d'une logique de construction en tuyau(pipeline) en utilisant le symbole pipeline(|)
-1.on regarde une ligne du fichier <access.log> pour reperer la colonne qui nous interesse: on constate que les <ip> sont sur la 1ere colonne
-2.<awk '{print $1}' access.log>: affiche une liste de 5000 ip brutes, les unes sous les autres
-3.<sort> va permettre de grouper les doublons(c'est un tri alphabetique)
-4.<uniq -c>: la commande <uniq>,sert a supprimer les lignes doublons consecutives et l'option <c> permet de compter les occurences de chaque ligne: resultat, une liste ou chaque IP unique est precedee du nombre de fois ou elle apparait.
-5.<sort -nr>:sert a trier les lignes par ordre numerique decroissant. l'option <n>, demande a <sort> de trier les elts en tant que nombre(ou 10 vient apres 2) et non en tant que texte(ou "10" viendrait avant "2" a cause de "1") et <r>, inverse l'ordre du tri pour aller du plus grand au plus petit.
-6.<head -n 5>: sert a eviter d'avoir des centaines de lignes qui defilent dans le terminal, on tronque le resultat avec <head>. ici <n> represente le nombre de ligne
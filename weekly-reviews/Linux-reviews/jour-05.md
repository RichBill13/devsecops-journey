## Gestion des processus sous Linux

## 5 types de processus
-interactif: lancer par l'utilisateur depuis un terminal ou une interface graphique(bash, firefox, top)

-Batch: Tache automatique planifiee executee en arriere plan(script de rotation de logs)

-Daemons: services d'arriere-plan permanents, souvent lances au demarrage(sshd, httpd, cupsd)

-Threads: sous-processus legers executes au sein d'un processus principal(gnome-terminal-server)

-Kernel Threads: taches internes gerees uniquement par le noyau(kthreadd, ksoftirqd)

## Etats d'un Processus
-R(Running/Runable): Processus en cours d'execution sur le CPU ou attend son tour
-S(interrutible Sleep): le processus dort/attend une action
-D(uninterruptible sleep): le processus attend une entree/sortie disque ou reseau et ne peut pas etre interrompu
-Z(Zombie): le processus enfant est terminee, mais le processus parent n'a pas encore lu son code de sortie.

## Trouver et Forcer l'arret d'un Processus(KILL)
-identifier le PID de l'application: trouver son numero PID avec la commande : ## pgrep firefox (ici on identifie direct l'app"firefoc")
/pour voir la liste complete: ## ps -eo pid,ppid,stat,comm

-Forcer l'arret avec kill -9 ou kill -SIGKILL <PID>

## Utilisateur et Groupe d'utilisateur
plusieurs personnes peuvent utiliser  un systeme au meme moment, et chacun peut executer plusieurs processus .
les utlisateurs peuvent aussi etre organises en groupe et chaque groupe possede un <RGID>(Real Group ID). Un utilisateur peut appartenir a un ou plusieurs groupes.

## Gestion des priorites d'execution des processus
-la priorite standard: la valeur de <Niceness>, de -20 a +19
-plage de valeurs: -20(priorite maximale), +19(priorite minimale)
-par defaut, tout nouveau processus demarre avec une valeur 0.
-un user standard peut seulement augmenter la niceness des ses propres processus(rendre les taches moins prioritaire)
-un admin(root/admin): indispensable pour donner une valeur negative(rendre la tache plus prioritaire) ou modifier les processus des autres utilisateurs.

## example
<nice -n 10 ./traitement_lourd.sh>: lancer un traitement lourd sans ralentir le systeme(priorite basse)
<sudo nice -n -5 ./tache.urgente.sh>:lance une tache critique (priorite haute-requiert sudo)
<renice -n 12 -p 4820>: change le priorite d'un processus deja en cours d'execution a partir de son PID(en le rendant moins prioritaire)
<sudo renice -n -8 -p 4820>(en le rendant plus prioritaire grace a sudo)

## Load Averages
le systeme de chargement(system load) mesure le nombre de taches active utilisant le CPU ou le nombre de taches sur la liste d'attente, attendant leur tour. ils en existe de 3 types:
-<Running>: en cour d'execution sur le CPU
-<Runnable>: pret a etre executer, mais attendant dans la queue pour un espace libre sur le CPU
-<Uninterruptible sleep(D state)>: en attente de ressources materiels(memoire sur le disque)

## les 3 chiffres du Load Average
lorsque tu tapes la commande uptime, w ou top , le systeme affiche 3 valeurs:
<load average: 0.45, 0.17. 0.12>
{
    -Premier chiffre(0.45): la moyenne sur la derniere minute.
    -Deuxieme chiffre(0.17): la moyenne sur les 5 dernieres minutes.
    -Troisieme chiffre(0.12): la moyenne sur les 15 dernieres minutes
}
Comparer ces trois chiffres permet de voir la tendance: si le premier chiffre est plus eleve que le dernier(ex: 4.5, 1.2, 0.5),la charge augmente. s'il est plus bas(ex: 0.5, 1.2, 4.5), le systeme se calme.

## La regle du multi-coeur
si une machine possede plusieurs coeurs processeur, il faut diviser le <load average> par le nombre de coeurs pour connaitre la vraie charge:
-sur un 4 coeurs
{
    -un load de 4.00 signifie que les 4 coeurs sont occupes a 100%(4/4=1.0=100%)
    -un load de 2.00 signifier que le systeme tourne a 50% de sa capacite globale
    -un load de 8.00 signifie qu'il y a 2 personnes en file d'attente sur chaque caisse
}

## Gestion des taches ( Job Control)

## commande &
execute la commande en tache de fond. le terminal affiche job ID(ex: [1]) et le PID puis rend la main immediatement

## Ctrl + C
arrete et termine definitivement la tache en cours dans le terminal

## Ctrl + Z
suspend la tache courant(etat <stopped>). la tache reste en memoire sans consommer de CPU.

## bg %N
reprend l'execution d'une tache suspendue(<stopped>) en arriere plan.

## fg %N
Ramene une tache d'arriere plan au premier plan

## jobs ou jobs -l
affiche la liste des taches gerees par le terminal actuel(-l ajoute le PID)

## ajouter &
lance le processus en arriere plan mais ne reduit pas sa priorite CPU.
Pour executer un traitement lourd sans ralentir votre machine, combinez avec <nice>(ex: nice -n 10 updatedb &)
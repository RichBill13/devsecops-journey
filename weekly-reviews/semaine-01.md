# Semaine 01 — Installation de l’environnement DevSecOps

## Informations générales

- Période : du 02/09/26 au 02/09/26
- Module étudié : Module 0
- Sujet principal : Mise en place de l’environnement de travail
- Statut : termine

---

## 1. Objectifs de la semaine

- Installer Ubuntu avec WSL2.
- Comprendre la différence entre Windows, PowerShell et Ubuntu.
- Installer les outils Linux essentiels.
- Configurer Git.
- Créer le dépôt `devsecops-journey`.
- Publier le projet sur GitHub.
- Comprendre les commandes utilisées.

---

## 2. Travaux réalisés

- [x] Activation de la virtualisation.
- [x] Installation de WSL2.
- [x] Installation d’Ubuntu.
- [x] Mise à jour d’Ubuntu.
- [x] Installation de Git et des outils essentiels.
- [x] Configuration de mon identité Git.
- [x] Création de la structure du projet.
- [x] Initialisation du dépôt Git.
- [x] Création du dépôt GitHub.
- [x] Authentification avec GitHub CLI.
- [x] Premier push vers GitHub.

---

## 3. Cours et explications

Je viens de construire mon environnement de travail DevSecOps sous Linux, de le versionner avec Git et de le sauvegarder sur GitHub. 

## 1. Installation de WSL2(Windows Subsystem for Linux) et Ubuntu

Mon ordinateur fonctionne sous Windows, mais la majorité des outils DevOps, Cloud et cybersécurité sont utilisés sous Linux.

WSL2 permet d’exécuter Ubuntu directement dans Windows, sans avoir besoin de démarrer une machine virtuelle VMware à chaque fois.

L’organisation est donc :

Windows : navigateur, Word, interface de VS Code, VMware.
Ubuntu WSL2 : commandes Linux, Git, Python, Docker, Terraform, Ansible et tes futurs projets.
VMware : laboratoires nécessitant plusieurs machines, Kali Linux ou des réseaux particuliers.

Quand tu vois :

PS C:\Users\USER>

tu es dans PowerShell.

Quand tu vois :

rich@DESKTOP-T2BABNH:~$

tu es dans Ubuntu.

C’est pour cette raison que touch ne fonctionnait pas dans PowerShell : c’est une commande Linux.

## 2. Activation de la virtualisation

Au début, WSL affichait :

HCS_E_HYPERV_NOT_INSTALLED

Cela signifiait que Windows ne pouvait pas démarrer la machine virtuelle légère utilisée par WSL2.

Nous avons activé le lancement de l’hyperviseur avec :

bcdedit /set hypervisorlaunchtype auto

Après le redémarrage, Windows a pu lancer Ubuntu avec WSL2.

## 3. Mise à jour d’Ubuntu

Nous avons exécuté :

sudo apt update
sudo apt upgrade -y

Voici la différence :

sudo : exécute une commande avec les droits administrateur.
apt update : récupère la liste récente des logiciels disponibles.
apt upgrade : installe les mises à jour disponibles.
-y : répond automatiquement « oui » aux confirmations.

Cela permet de commencer avec un système propre et à jour.

## 4. Installation des outils essentiels

Nous avons installé :

## sudo apt install -y git curl wget unzip tree build-essential
Outil	Utilité
git	    Enregistrer et suivre les modifications de tes projets
curl	Communiquer avec des sites et des API depuis le terminal
wget	Télécharger des fichiers
unzip	Décompresser des fichiers ZIP
tree	Afficher visuellement l’arborescence d’un projet
build-essential	Compiler certains programmes sous Linux

Tu ne maîtrises pas encore nécessairement tous ces outils. Nous les avons installés parce qu’ils seront régulièrement utilisés dans les prochains modules.

## 5. Configuration de ton identité Git(systeme de gestion des version, il conserve l'historique des modifications apportees a mes fichier et a mes projets.)

Nous avons configuré :

git config --global user.name "Rich Kamdem"
git config --global user.email "ton-adresse@email.com"
git config --global init.defaultBranch main

Git inscrit un auteur dans chaque modification enregistrée.

user.name indique ton nom.
user.email associe tes contributions à ton adresse.
init.defaultBranch main demande à Git d’appeler la branche principale main.
--global applique cette configuration à tous tes futurs projets Ubuntu.

## 6. Création de ton espace de travail

Nous avons créé :

/home/rich/devsecops-journey

Le symbole ~ représente ton dossier personnel :

/home/rich

Ainsi :

cd ~/devsecops-journey

signifie :

Aller dans /home/rich/devsecops-journey.

Nous avons volontairement placé le projet dans Ubuntu et non dans :

/mnt/c/Users/...

Cela apporte généralement de meilleures performances et évite certains problèmes de permissions entre Windows et Linux.

## 7. Organisation du projet

Ton projet contient normalement cette structure :

devsecops-journey/
├── archive/
├── labs/
├── notes/
├── projects/
├── weekly-reviews/
├── README.md
├── later.md

Chaque élément a un rôle :

projects/ : tes projets complets.
labs/ : tes exercices pratiques.
notes/ : tes notes techniques.
weekly-reviews/ : tes bilans hebdomadaires conserver dans des fichiers semaine-01 etc.
archive/ : les anciens travaux conservés.
README.md : présentation générale de ton parcours.
later.md : technologies intéressantes, mais reportées pour éviter la dispersion.

La commande :

mkdir -p ~/devsecops-journey/{projects,labs,notes,weekly-reviews,archive}

a créé tous ces dossiers en une seule fois.

La commande :

touch README.md roadmap.md later.md journal.md

a créé les fichiers vides.

## 8. Transformation du dossier en dépôt Git

Nous avons exécuté :

## git init

Cette commande transforme un dossier ordinaire en dépôt Git.

À partir de là, Git peut surveiller les fichiers et conserver l’historique de leurs modifications.

Les commandes importantes sont :

## git status

Affiche les fichiers modifiés, nouveaux ou prêts à être enregistrés.

## git add .

Place toutes les modifications dans la zone de préparation. Cela signifie : « Je veux inclure ces changements dans le prochain enregistrement. »

## git commit -m "Document module 0 workflow"

Crée un point précis dans l’historique du projet. Un commit est comme une photographie du projet à un moment donné.

## git log --oneline

Affiche l’historique résumé des commits.

## 9. Utilisation de VS Code avec Ubuntu

Nous avons lancé :

## code .
code ouvre VS Code.
. représente le dossier actuel.

L’interface de VS Code fonctionne sous Windows, mais elle est connectée à Ubuntu grâce à WSL. C’est pourquoi tu dois vérifier la présence de :

WSL: Ubuntu

Tu peux donc profiter de l’interface graphique de Windows tout en exécutant tes commandes et programmes dans Linux.

## 10. Pourquoi Git affichait « dubious ownership »

Tu avais lancé :

git status

depuis PowerShell dans un dossier Ubuntu :

\\wsl.localhost\Ubuntu\home\rich\devsecops-journey

Windows Git essayait donc de manipuler un dépôt appartenant au système Linux. Par sécurité, Git a signalé une différence de propriétaire.

Nous n’avons pas ajouté l’exception proposée. Nous avons simplement utilisé le bon Git : celui installé dans Ubuntu.

La règle est donc :

Si le projet se trouve dans /home/rich, les commandes Git doivent être exécutées dans Ubuntu.

## 11. Création du dépôt GitHub

Git enregistre l’historique sur ton ordinateur. GitHub conserve une copie distante sur Internet.

Nous avons relié les deux avec :

## git remote add origin https://github.com/TON_USERNAME/devsecops-journey.git
remote : dépôt distant.
origin : nom court donné à ton dépôt GitHub.
l’adresse HTTPS : emplacement réel du dépôt.

Tu peux vérifier cette connexion avec :

git remote -v

## 12. Authentification avec GitHub CLI

GitHub n’accepte pas le mot de passe du compte pour un git push en HTTPS.

Nous avons donc installé :

## sudo apt install gh -y

Puis lancé :

## gh auth login

gh est l’outil officiel permettant de communiquer avec GitHub depuis le terminal. L’authentification par navigateur a autorisé Ubuntu à accéder à ton compte sans placer ton mot de passe dans une commande.

Tu peux vérifier la connexion avec :

gh auth status

## 13. Publication avec git push

La commande finale était :

## git push -u origin main

Elle signifie :

push : envoyer les commits vers GitHub.
origin : dépôt GitHub destinataire.
main : branche envoyée.
-u : mémoriser la relation entre la branche locale et celle de GitHub.

Grâce à -u, les prochains envois pourront simplement utiliser :

git push

---

### Entrer dans Ubuntu depuis PowerShell

```powershell
wsl
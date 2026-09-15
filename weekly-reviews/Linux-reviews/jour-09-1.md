## Introduction au reseautage
<un reseau>: est un ensemble d'ordinateurs et de peripheriques informatiques connectes entre eux par des cannaux de communication, tels que des cables ou des liaisons sans fil.
-il sert a autoriser les appareils connectes a communiquer entre eux.
-permettre a plusieurs users de partager des peripheriques sur le reseau, tels que des serveurs de musique et de video, des imprimantes et des scanners
-partager et gerer facilement des informations telles que des bases de donnees et des systemes de fichiers entre ordinateurs.

## Adresse IP(internet protocol)
chaque appareil connecte a un reseau doit en posseder au moins une, elle est indispensable pour l'acheminement des paquets de donnees sur le reseau.

les paquets contiennent des tampons de donnees, ainsi que des en-tetes indiquant leur destination, leur origine et leur position dans la sequence de paquets constituant le flux.

## IPV4 & IPV6
se sont les deux types d'adresse qui existe, l'ipv4 est plus ancienne et de loin la plus repandue, tandis que l'ipv6 est plus recente et a ete concu pour pallier les limitations inherentes a l'ancienne norme et fournir un nombre d'adresses beaucoup plus important.

le protocole ipv4 utilise des adresses 32bits; seuls 4.3 milliards d'adresses unique sont dispo
tandis que le protocole ipv6 lui utilise des adresses de 128bits ce qui permet d'attribuer 3.4 * 10 puissance 38 adresses.

## Decodage des adresses IPV4
une adresse <ipv4> de 32bits est divisee en quatre sections de 8 bits appelees <octets>
ex: 
Adresse IP--> 172.16.31.46
Format binaire --> 10101100.00010000.00011111.00101110

les adresses reseau sont divisees en cinq classes: A,B,C,D,E. Les classes A,B et C se composent de deux parties: <l'adresse reseau> (identifiant reseau) et <l'adresse hote>(identifiant hote).
l'identifiant reseau permet d'identifier le reseau, tandis que l'identifiant hote permet d'identifier un hote au sein de ce reseau. la classe D est utilise pour des applications de  multidiffusion specifiques, et la classe E est reservee pour un usage futur.

## Adresses reseau de classe A
-ils utilisent le premier octet d'une adresse IP comme identifiant de reseau et les trois autres comme identifiant d'hote.
-le premier bit  du premier octet est toujours a 0, on ne peut donc utiliser que 7 bits pour un numero de reseau unique. Par consequent, il existe au max 126 reseaux de classe A dispo(les adresses 0000000 et 1111111)
-chaque reseau de classe A peut compter jusqu'a 16.7 millions d'hotes uniques. la plage d'adresses IP des hotes s'etend de <1.0.0.0> a <255.255.255.255>
NB: la valeur d'un octet, ou de 8 bits, peut aller de 0 a 255

## Adresses reseau de classe B
-leurs adresses commencent par 10
-plage: <128.0.0.0> a <191.255.255.255>
-reseau.reseau.hote.hote
-16384 en moyenne de nombres de reseaux
-65534 en moyenne de nombre d'hotes

## Adresses reseau de classe C
-leur adresses commencent par 110
-plage: <192.0.0.0> a <223.255.255.255>
-reseau.reseau.reseau.hote
-2097152 en moyenne de nombres de reseaux
-254 en moyenne de nombre d'hote

## Attribution d'adresse IP
En general, l'admin du reseau demande une plage d'adresses IP a notre fournisseur d'acces internet(FAI). le choix de la classe d'adresse qui va etre attribue depend de la taille du reseau et surtout des besoind de croissances prevus.
-cette attribution peut se faire soit manuellement ou dynamiquement. l'ajout manuelle ajoute des adresses statique(qui ne changent jamais) au reseau. l'ajout dynamique ajoute des adresses qui peuvent changer a chaque redemarrage, vour plus frequemment.
-le protocole <DHCP>(Dynamic Host Configuration Protocol) est utilise pour l'attribution des adresses IP.

## Resolution de nom
cette etape permet de convertir les adresses IP numeriques en un format lisible par l'humain, appele <nom d hote>.
ex: 3.13.31.214 est l'adresse IP numerique qui correspond au nom d'hote <linuxfoundation.org>
ex: <127.0.0.1> est l'adresse IP numerique qui correspond au nom d'hote <localhost>

## Fichiers de config reseau
les fichiers de configuration reseau sont indispensable au bon fonctionnement des interfaces. il se trouve dans l'aborescence </etc> ou plus precisement </etc/network>.

## interface reseau
les interfaces reseau constituent un canal de connexion entre un peripherique et un reseau
-<ip> et <ipcongif> permettent d'obtenir des informations sur une interface reseau particuliere ou sur l'ensemble des interfaces reseau.-
-<ip addr show>: permet d'afficher l'adresse IP
-<ip route show>:permet de consulter les informations d'itineraire

## ping
cette commande permet de verifier si une machine connectee au reseau peut recevoir et envoyer des donnees; autrement dit, elle confirme que l'hote distant est en ligne et repond.
-<ping nomhote>: pour verifier l'etat de l'hote distant

## route
un reseau necessite la connexion de nombreux noeuds. Les donnees transitent de la source a la destination en passant par une serie de routeurs et potentiellement par plusieurs reseaux. les serveurs gerent des tables de routage contenant les adresses de chaque noeud du reseau. Les protocoles de routage IP permettent aux routeurs de construire une table de transfert qui associe les destinations finales aux adresses des prochains sauts
-<ip route>: permet d'afficher ou de modifier la table de routage IP afin d'ajouter, de supprimer ou de modifier des routes statiques vers des hotes ou des reseaux specifiques.
-<ip route add>: ajoute une route statique
-<ip route del>: supprime une route statique

## traceroute
cette commande permet d'inspecter le chemin emprunte par un paquet de donnees pour atteindre l'hote de destination, ce qui la rend tres utile pour diagnostiquer les problemes de latence et d'erreurs reseau <traceroute adresse>

## Plus d'outils de reseautage
ces outils sont tres utiles pour surveiller et deboguer les problemes de reseau, tels que la connectivite et le trafic reseau.
-<ethtool>: interroge les interfaces reseau et peut egalement definir divers parametres tels que la vitesse
-<netstat>: Affiche toutes les connexions actives et les tables de routage
-<nmap>: Analyse les ports ouverts sur un reseau; important pour l'analyse de securite
-<tcpdump>: Analyse le trafic reseau en aval
-<iptraf>: surveille le trafic reseau en mode texte
-<mtr>: combine les fonctionnalites de ping et de traceroute et fournit un affichage mis a jour en continu
-<creuser>: teste le fonctionnement du DNS

## wget 
cette commande permet de telecharger des fichiers et des informations ou encore des repertoires depuis la ligne de commande ou un script
-<wget url>: permet de telecharger une page web, ensuite de lire la page telechargee comme un fichier local a l'aide d'un navigateur graphique(firefox, chrome) ou non graphique (lynx, elinks, w3m)

## curl
-<curl url>: permet de lire une url 
-<curl -o nom.html url>: permet de recuperer le contenu d'une page web(url) et l'enregistrer dans un fichier (nom.html)

## FTP(File Transfert Protocol)/ protocole de transfert de fichiers
Lorsque vous etes connectes a un reseau, vous pouvez avoir besoin de transferer des fichiers d'un ordinateur a un autre. le protocole de transfert des fichiers (FTP) est une methode courante pour transferer des fichiers entre ordinateurs via internet. elle repose sur le modele client-serveur.

## SSH: Execution de commandes a distance
secure shell (SSH) est un protocole reseau cryptographique utilise pour la communication de donnees securisee. il est egalement utilise pour les services a distance et autres services securises entre   appareils du reseau, et s'avere tres utile pour administrer des systemes difficiles d'acces physiquement, mais auxquels vous avez un acces a distance.
-<ssh somesystem>: permet de connecter a un systeme distant avec mon nom d'utilisateur habituel

## Copie de fichiers securisee avec scp
il est possible de transferer des fichiers en toute securite entre deux hotes du reseau a l'aide de <secure cop(scp)>, il utilise le protocole SSH pour le transfert de donnees.
-<scp fichierlocal utilisateur@systemedistant:/home/utilisateur>
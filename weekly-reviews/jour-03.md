## Jour 03- introduction a linux (lfs 101)

## 01 Comment les mots de passe sont stockes
 a l'epoque les mdp etaient stockes dans le fichier /etc/passwd qui etait accessible a tous , facilitant ainsi leur piratage.
 sous les sytemes moderne ce n'est plus le cas ils sont desormais stockes sous forme chiffree et dans un fichier secondaire /etc/shadow. 
 seuls les users disposant des droits admin(root), peuvent lire ou modifier ce fichier.

 ## 02 Cryptage des mots de passe

 la plupart des distributions linux utilisent un algorithme de chiffrement moderne appele SHA-512(Secure Hashing Algorithme 512bits) developpe par la NSA pour chiffrer les mots de passe.
 l'algorithme SHA-512 est largement utilise dans les applications et protocoles de securite, notamment TLS, SSL, PHP, SSH, S/MIME etc.

 ## 03 Bonne pratiques en matiere de mots de passe

 -renouvellement automatique des mdp: envoi de notifications aux user leurs demandant de creer un nouveau mdp(ainsi meme en cas de piratage, les mdp ne seront utilisables que pendant une duree limitee.)
 -imposer aux users une definitions de mdp robustes grace aux modules d'authentification enfichables(PAM)(les PAM sont configurer pour verifier la robustesse des mdp crees ou modifiees avec l'utilitaire passwd. leurs configuration se fait via les bibliotheque pam_cracklib.so ou pam_passwdqc.so)
 -installation de logiciels de piratage de mpd(JOHN THE RIPPER) afin de securiser le fichier de mots de passe et de detecter les mdp faibles.
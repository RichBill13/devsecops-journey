## un Log(fichier journal)
c'est un fichier texte genere automatiquement par un systeme, une application ou un serveur pour enregistrer chronologiquement tous les evenements, actions ou erreurs qui s'y produisent.

## A quoi sert un bug
-<le debogage(Debugging)>: comprendre l'origine d'un bug ou le plantage d'un programme
-<la surveillance(Monitoring)>: Verifier l'etat de sante d'un serveur ou d'une application en temps reel
-<la securite et l audit>: detecter les tentatives d'intrusion, analyser les connexions suspectes, savoir qui a fait quoi et quand.
-<l'analyse de performance>: mesurer le temps de reponse ou le traffic d'un site web.

## structure d'un log
-[horodatage][niveau de severite][composant/module]message d'evenement.

## les differents niveau de logs
-<DEBUG>: informations tres detailles pour les developpeurs lors de la phase de developpement.
-<INFO>:evenement normal d'un systeme(utilisateur connecte, service demarre)
-<WARNING/WARN>: avertissement sur une anomalie non bloquante
-<ERROR>: erreur empechant une action specifique de s'accomplir sans arreter toute l'application
-<FATAL/CRITICAL>: erreur grave provoquant l'arret complet de l'application ou du systeme

## grep
sert a filtrer des lignes par mot cle
## sed
modifie/remplace du texte
## awk
sert a extraire et analyser les colonnes
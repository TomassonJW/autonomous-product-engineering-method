# Runtime de worker autonome

Un worker autonome n'est pas seulement un modèle avec un long prompt. C'est un pattern de runtime borné.

## Éléments requis

Un worker durable a besoin :

- d'une mission ;
- d'un owner ;
- d'une queue ou liste de tâches ;
- de limites de scope ;
- d'une zone de sécurité ;
- d'une politique de budget ;
- d'un fichier ou endpoint de statut ;
- de logs ;
- de checkpoints ;
- de gates qualité ;
- d'un fichier ou condition d'arrêt ;
- de notes de rollback ;
- d'un timeout ;
- d'une stratégie de notification ;
- d'un rapport final ;
- d'une gestion des approbations externes.

## Mission worker

Une mission worker doit dire :

- ce que le succès signifie ;
- ce qui est hors scope ;
- quels fichiers, systèmes ou outils peuvent être touchés ;
- quelles actions sont interdites ;
- quelles preuves sont requises ;
- quand s'arrêter et demander ;
- comment rapporter un progrès partiel.

## Pattern superviseur

Le worker ne doit pas être seul juge de son succès.

Un wrapper, superviseur ou reviewer humain doit pouvoir :

- rejeter une complétion prématurée ;
- faire respecter temps et quotas ;
- capturer les logs ;
- détecter les boucles d'échec répétées ;
- mettre en pause ou arrêter le run ;
- vérifier les gates ;
- envoyer les notifications finales ;
- préserver les preuves.

## Pattern checkpoint

Le travail long doit être divisé en checkpoints :

1. Contexte chargé.
2. Plan accepté ou borné.
3. Premier artefact créé.
4. Tests ou audits lancés.
5. Risques mis à jour.
6. Rapport final préparé.

Chaque checkpoint doit enregistrer ce qui a changé, ce qui reste incertain et quelle action est autorisée ensuite.

## Faux succès

Un faux succès se produit quand un worker rapporte la complétion sans preuve.

Exemples :

- "Tests passés" sans sortie de test.
- "Production-ready" sans gates de déploiement.
- "Publié" sans vérifier l'URL publique.
- "Sûr" sans scan de secrets ni approbation d'action rouge.

Le runtime doit traiter le faux succès comme un mode d'échec, pas comme un style de communication.
